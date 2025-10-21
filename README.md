# 🚀 Trading Strategy API - FastAPI & Moving Average Crossover

<div align="center">

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Tests](https://img.shields.io/badge/tests-8/8%20passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

**A professional trading application with real HINDALCO data and moving average crossover strategy**

</div>

## 📊 Project Overview

This project implements a complete trading strategy API with:
- **1216 real HINDALCO records** (2014-2018 daily data)
- **Moving Average Crossover Strategy** (10-day/30-day)
- **FastAPI RESTful endpoints** with automatic documentation
- **SQLite database** with Prisma schema
- **Docker containerization**
- **Comprehensive unit testing** (8/8 tests passing)

## 🚀 Quick Start

### Local Development
```bash
# Clone repository
git clone https://github.com/ashutoshpandey18/trading-app.git
cd trading-app

# Install dependencies
pip install -r requirements.txt

# Run application
python final_app.py

# Access the API at http://localhost:8000
# View documentation at http://localhost:8000/docs

Docker Deployment

# Build and run with Docker
docker build -t trading-app .
docker run -p 8000:8000 trading-app

# Or use Docker Compose
docker-compose up

📡 API Endpoints
GET / - API information & endpoints
GET /data - Get all 1215 HINDALCO records
POST /data - Add new stock data with JSON payload
GET /strategy/performance - Trading strategy results with short_window and long_window parameters
GET /strategy/signals - Recent trading signals with short_window and long_window parameters
GET /health - System health check
GET /docs - Interactive API documentation

📈 Trading Strategy

Moving Average Crossover Strategy:

Short Window: 10-day moving average

Long Window: 30-day moving average

Buy Signal: When short MA crosses above long MA

Sell Signal: When short MA crosses below long MA

Performance Metrics:

Total Trades: Number of executed trades

Win Rate: Percentage of profitable trades

Total Return: Overall strategy performance

Recent Signals: Last 10 trading signals with timestamps

🧪 Testing

# Run complete test suite
python -m pytest app/tests/ -v

# Expected output: 8 tests passing

Test Coverage
✅ API endpoint validation
✅ Moving average calculations
✅ Strategy performance metrics
✅ Error handling scenarios
✅ Input validation tests

📸 Screenshots
<div align="center">
API Documentation
https://Screenshot%25202025-10-21%2520041740.png
Interactive Swagger UI with automatic endpoint documentation

HINDALCO Data (1215 Records)
https://Screenshot%25202025-10-21%2520041539.png
*Real HINDALCO daily stock data from 2014-2018*

Trading Strategy Performance
https://Screenshot%25202025-10-21%2520041553.png
Moving average crossover strategy results and analytics

Docker Deployment
https://Screenshot%25202025-10-21%2520040655.png
Containerized application build and execution process

Test Results
https://Screenshot%25202025-10-21%2520050648.png
*Comprehensive test suite with 8/8 tests passing*

</div>
🔧 Technical Stack
Backend Framework: FastAPI

Programming Language: Python 3.8+

Database: SQLite with Prisma ORM

Testing Framework: Pytest + unittest

Containerization: Docker + Docker Compose

API Documentation: Swagger UI (Auto-generated)

Data Validation: Pydantic

HTTP Server: Uvicorn

📊 Database Schema

model StockData
{
  id       Int      @id @default(autoincrement())
  datetime DateTime @unique
  open     Float
  high     Float
  low      Float
  close    Float
  volume   Int
}

Sample Data Structure

{
  "id": 1,
  "datetime": "2014-01-01T00:00:00",
  "open": 150.25,
  "high": 152.50,
  "low": 149.75,
  "close": 151.80,
  "volume": 1000000
}

🐳 Docker Configuration

Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python","final_app.py"]

Docker Compose

version: '3.8'
services:
  trading-app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=sqlite:///trading_final.db

🔄 API Usage Examples

Get All Stock Data

curl -X GET "http://localhost:8000/data"

Get Strategy Performance

curl -X GET "http://localhost:8000/strategy/performance?short_window=10&long_window=30"

Add New Data

curl -X POST "http://localhost:8000/data" \
  -H "Content-Type: application/json" \
  -d '{
    "datetime": "2024-01-01T10:00:00",
    "open": 150.0,
    "high": 155.0,
    "low": 148.0,
    "close": 152.5,
    "volume": 1000000
  }'

  Health Check

  curl -X GET "http://localhost:8000/health"

  🛠️ Development Setup
Prerequisites
Python 3.8 or higher

Docker (optional, for containerization)

Git

Installation Steps
Clone the repository

Install Python dependencies

Run the application

Access API documentation

Environment Variables

env :

DATABASE_URL=sqlite:///trading_final.db

<<<<<<< HEAD
=======

👨‍💻 Author
Your Ashutosh Pandey

GitHub: @ashutoshpandey18

Email: ashutoshpandey23june2005@gmail.com
>>>>>>> e869f3bdbe3a5c5a3d7900dece19b60ff2759def
