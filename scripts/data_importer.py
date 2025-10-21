"""Data import utility for HINDALCO stock data"""
import pandas as pd
import asyncio
import sys
import os
from datetime import datetime
from pathlib import Path

# Add app to Python path
sys.path.append(str(Path(__file__).parent.parent))

from app.database import db_manager

class DataImporter:
    """Handles importing stock data from various file formats"""

    def __init__(self):
        self.supported_formats = ['.csv', '.xlsx', '.xls']

    def find_data_file(self) -> str:
        """Find HINDALCO data file in project directory"""
        project_root = Path(__file__).parent.parent

        for file_format in self.supported_formats:
            pattern = f"*HINDALCO*{file_format}"
            matches = list(project_root.glob(pattern))
            if matches:
                return str(matches[0])

        raise FileNotFoundError(
            f"No HINDALCO data file found. "
            f"Supported formats: {', '.join(self.supported_formats)}"
        )

    def load_data(self, file_path: str) -> pd.DataFrame:
        """Load data from file based on format"""
        file_ext = Path(file_path).suffix.lower()

        if file_ext == '.csv':
            return pd.read_csv(file_path)
        elif file_ext in ['.xlsx', '.xls']:
            return pd.read_excel(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_ext}")

    def preprocess_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Preprocess and validate stock data"""
        # Standardize column names
        column_mapping = {}
        for col in df.columns:
            col_lower = str(col).lower()
            if 'date' in col_lower or 'time' in col_lower:
                column_mapping[col] = 'datetime'
            elif 'open' in col_lower:
                column_mapping[col] = 'open'
            elif 'high' in col_lower:
                column_mapping[col] = 'high'
            elif 'low' in col_lower:
                column_mapping[col] = 'low'
            elif 'close' in col_lower:
                column_mapping[col] = 'close'
            elif 'volume' in col_lower:
                column_mapping[col] = 'volume'

        df = df.rename(columns=column_mapping)

        # Validate required columns
        required_columns = ['datetime', 'open', 'high', 'low', 'close', 'volume']
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

        # Convert datetime
        df['datetime'] = pd.to_datetime(df['datetime'])

        # Validate numeric columns
        numeric_columns = ['open', 'high', 'low', 'close', 'volume']
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Remove rows with invalid data
        df = df.dropna()

        # Validate data ranges
        if (df[['open', 'high', 'low', 'close']] <= 0).any().any():
            raise ValueError("Price values must be positive")

        if (df['volume'] <= 0).any():
            raise ValueError("Volume values must be positive")

        return df

    async def import_data(self) -> int:
        """Main import method"""
        try:
            # Find and load data file
            file_path = self.find_data_file()
            print(f"📁 Found data file: {file_path}")

            df = self.load_data(file_path)
            print(f"📊 Loaded {len(df)} rows with columns: {list(df.columns)}")

            # Preprocess data
            df_processed = self.preprocess_data(df)
            print("✅ Data preprocessing completed")

            # Connect to database
            await db_manager.connect()

            # Clear existing data
            await db_manager.client.stockdata.delete_many()
            print("🗑️ Cleared existing data")

            # Import data
            imported_count = 0
            for _, row in df_processed.iterrows():
                try:
                    await db_manager.client.stockdata.create(
                        data={
                            'datetime': row['datetime'],
                            'open': float(row['open']),
                            'high': float(row['high']),
                            'low': float(row['low']),
                            'close': float(row['close']),
                            'volume': int(row['volume'])
                        }
                    )
                    imported_count += 1

                    if imported_count % 50 == 0:
                        print(f"⏳ Imported {imported_count} records...")

                except Exception as e:
                    print(f"⚠️ Skipping row {imported_count}: {e}")
                    continue

            print(f"🎉 Successfully imported {imported_count} records")
            return imported_count

        except Exception as e:
            print(f"❌ Import failed: {e}")
            raise
        finally:
            await db_manager.disconnect()

async def main():
    """Main execution function"""
    print("🚀 HINDALCO Data Import Utility")
    print("=" * 50)

    importer = DataImporter()

    try:
        count = await importer.import_data()
        print(f"\n✅ Import completed: {count} records imported")
    except Exception as e:
        print(f"\n❌ Import failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())