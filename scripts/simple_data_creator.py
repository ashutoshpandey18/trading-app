"""Create sample data without pandas"""
import asyncio
from datetime import datetime, timedelta
import random
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import db_manager

async def create_sample_data():
    """Create realistic sample stock data"""
    print("📊 Creating sample stock data...")

    await db_manager.connect()

    # Clear existing data
    await db_manager.client.stockdata.delete_many()

    # Generate 100 days of realistic data
    base_price = 100.0
    base_volume = 1000000
    records_created = 0

    for i in range(100):
        date = datetime(2023, 1, 1) + timedelta(days=i)

        # Realistic price movement
        change = random.uniform(-2.0, 2.5)
        base_price = max(50.0, base_price + change)  # Prevent going too low

        try:
            await db_manager.client.stockdata.create({
                'datetime': date,
                'open': round(base_price, 2),
                'high': round(base_price + random.uniform(0.5, 2.0), 2),
                'low': round(base_price - random.uniform(0.3, 1.5), 2),
                'close': round(base_price + random.uniform(-0.5, 0.5), 2),
                'volume': int(base_volume + random.uniform(-100000, 200000))
            })
            records_created += 1
        except Exception:
            continue

    print(f"✅ Created {records_created} sample records")
    await db_manager.disconnect()
    return records_created

if __name__ == "__main__":
    asyncio.run(create_sample_data())