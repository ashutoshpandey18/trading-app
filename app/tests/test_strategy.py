"""Trading strategy tests"""
import unittest
import sys
import os
from datetime import datetime, timedelta

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from final_app import TradingStrategy

class TestTradingStrategy(unittest.TestCase):
    """Test cases for trading strategy implementation"""

    def test_moving_average_calculation(self):
        """Test moving average calculations"""
        prices = [100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0]

        # Test short window
        short_ma = TradingStrategy.calculate_moving_average(prices, 5)
        self.assertEqual(len(short_ma), len(prices))
        self.assertEqual(short_ma[0], 0.0)  # Not enough data
        self.assertEqual(short_ma[4], 102.0)  # (100+101+102+103+104)/5

        # Test long window
        long_ma = TradingStrategy.calculate_moving_average(prices, 10)
        self.assertEqual(long_ma[9], 104.5)  # (100+101+...+109)/10

    def test_moving_average_edge_cases(self):
        """Test moving average with edge cases"""
        # Empty list
        result = TradingStrategy.calculate_moving_average([], 5)
        self.assertEqual(result, [])

        # Single element
        result = TradingStrategy.calculate_moving_average([100.0], 5)
        self.assertEqual(result, [0.0])

        # Window larger than data
        result = TradingStrategy.calculate_moving_average([1.0, 2.0], 5)
        self.assertEqual(result, [0.0, 0.0])

    def test_strategy_performance_structure(self):
        """Test strategy performance calculation returns correct structure"""
        # Create mock database-like data
        mock_data = []
        base_price = 100.0

        for i in range(50):  # Enough data for testing
            date = (datetime(2023, 1, 1) + timedelta(days=i)).isoformat()
            mock_data.append((
                i,  # id
                date,  # datetime
                base_price,  # open
                base_price + 2.0,  # high
                base_price - 1.0,  # low
                base_price + 1.0,  # close
                1000000  # volume
            ))
            base_price += 0.5

        # Test with sufficient data
        performance = TradingStrategy.calculate_strategy_performance(mock_data, 5, 20)

        # Verify structure
        self.assertIsInstance(performance.total_trades, int)
        self.assertIsInstance(performance.winning_trades, int)
        self.assertIsInstance(performance.losing_trades, int)
        self.assertIsInstance(performance.win_rate, float)
        self.assertIsInstance(performance.total_return, float)
        self.assertIsInstance(performance.signals, list)

        # Verify logical constraints
        self.assertTrue(0 <= performance.win_rate <= 1)
        self.assertEqual(
            performance.total_trades,
            performance.winning_trades + performance.losing_trades
        )

    def test_strategy_insufficient_data(self):
        """Test strategy with insufficient data"""
        mock_data = [(i, f"2023-01-{i+1:02d}T00:00:00", 100.0, 101.0, 99.0, 100.5, 1000000)
                    for i in range(10)]  # Only 10 records

        performance = TradingStrategy.calculate_strategy_performance(mock_data, 5, 20)

        self.assertEqual(performance.total_trades, 0)
        self.assertEqual(performance.winning_trades, 0)
        self.assertEqual(performance.losing_trades, 0)
        self.assertEqual(performance.win_rate, 0.0)
        self.assertEqual(performance.total_return, 0.0)
        self.assertEqual(performance.signals, [])

if __name__ == '__main__':
    unittest.main()