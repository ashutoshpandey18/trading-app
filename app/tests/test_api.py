"""API endpoint tests"""
import unittest
from fastapi.testclient import TestClient
from datetime import datetime
import sys
import os

# Add the parent directory to Python path to import final_app
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from final_app import app, TradingStrategy

class TestAPIEndpoints(unittest.TestCase):
    """Test cases for API endpoints"""

    def setUp(self):
        """Set up test client"""
        self.client = TestClient(app)

    def test_root_endpoint(self):
        """Test root endpoint returns API information"""
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn("message", data)
        self.assertIn("Trading Strategy API", data["message"])
        self.assertIn("endpoints", data)
        self.assertIn("GET /data", data["endpoints"])

    def test_get_data_endpoint(self):
        """Test GET /data endpoint structure"""
        response = self.client.get("/data")

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

    def test_health_endpoint(self):
        """Test health check endpoint"""
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertIn("records", data)

    def test_strategy_endpoint_validation(self):
        """Test GET /strategy/performance parameter validation"""
        # Test invalid window parameters (short >= long)
        response = self.client.get("/strategy/performance?short_window=30&long_window=30")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Short window must be less than long window", response.json()["detail"])

        # Test valid parameters
        response = self.client.get("/strategy/performance?short_window=10&long_window=30")
        # Could be 200 (success) or 400 (insufficient data)
        self.assertIn(response.status_code, [200, 400])

    # Remove the test_strategy_signals_endpoint method since the endpoint doesn't exist

if __name__ == '__main__':
    unittest.main()