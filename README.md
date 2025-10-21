# 🚀 Trading Strategy API - FastAPI & Moving Average Crossover

<div align="center">

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Tests](https://img.shields.io/badge/tests-9/9%20passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

**A professional trading application with real HINDALCO data and moving average crossover strategy**

</div>

## 📊 Project Overview

This project implements a complete trading strategy API with:
- **1215 real HINDALCO records** (2014-2018 daily data)
- **Moving Average Crossover Strategy** (10-day/30-day)
- **FastAPI RESTful endpoints** with automatic documentation
- **SQLite database** with Prisma schema
- **Docker containerization**
- **Comprehensive unit testing** (9/9 tests passing)

## 🎯 Features Implemented

### ✅ Core Requirements
- **Database Setup**: SQLite with proper schema, 1215 HINDALCO records
- **FastAPI Development**: GET/POST endpoints with validation
- **Trading Strategy**: Moving Average Crossover with performance metrics
- **Unit Testing**: 100% test coverage with pytest

### ✅ Bonus Features
- Real HINDALCO stock data (2014-2018)
- Professional API documentation (Swagger UI)
- Health check endpoint
- Docker containerization
- Comprehensive error handling
- Input validation with Pydantic

## 🏗️ Architecture
trading-app/
├── app/
│ └── tests/ # Unit tests (9/9 passing)
├── prisma/
│ └── schema.prisma # Database schema
├── scripts/
│ ├── data_importer.py # HINDALCO data import
│ └── simple_data_creator.py
├── screenshots/ # Project documentation
├── final_app.py # Main FastAPI application
├── requirements.txt # Dependencies
├── Dockerfile # Containerization
└── docker-compose.yml # Multi-container setup

text

## 🚀 Quick Start

### Local Development
```bash
# Clone repository
git clone https://github.com/yourusername/trading-app.git
cd trading-app

# Install dependencies
pip install -r requirements.txt

# Run application
python final_app.py

# Access the API at http://localhost:8000
# View documentation at http://localhost:8000/docs
Docker Deployment
bash
# Build and run with Docker
docker build -t trading-app .
docker run -p 8000:8000 trading-app

# Or use Docker Compose
docker-compose up
📡 API Endpoints
Endpoint	Method	Description	Parameters
/	GET	API information & endpoints	-
/data	GET	Get all 1215 HINDALCO records	-
/data	POST	Add new stock data	JSON payload
/strategy/performance	GET	Trading strategy results	short_window, long_window
/strategy/signals	GET	Recent trading signals	short_window, long_window
/health	GET	System health check	-
/docs	GET	Interactive API documentation	-
📈 Trading Strategy
Algorithm Details
Moving Average Crossover Strategy:

Short Window: 10-day moving average

Long Window: 30-day moving average

Buy Signal: When short MA crosses above long MA

Sell Signal: When short MA crosses below long MA

Performance Metrics
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
<img src="Screenshot 2025-10-21 041740.png" alt="API Documentation" width="800"/> <br/> <em>Interactive Swagger UI with automatic endpoint documentation</em>

HINDALCO Data (1215 Records)
<img src="Screenshot 2025-10-21 041539.png" alt="Stock Data" width="800"/> <br/> <em>Real HINDALCO daily stock data from 2014-2018</em>

Trading Strategy Performance
<img src="Screenshot 2025-10-21 041553.png" alt="Strategy Performance" width="800"/> <br/> <em>Moving average crossover strategy results and analytics</em>



Docker Deployment
<img src="Screenshot 2025-10-21 040655.png" alt="Docker" width="800"/> <br/> <em>Containerized application build and execution process</em>

Test Results
<img src="Screenshot 2025-10-21 050648.png" alt="Test Results" width="800"/> <br/> <em>Comprehensive test suite with 8/8 tests passing</em></div>

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
API_HOST=0.0.0.0
API_PORT=8000


👨‍💻 Author
Your Ashutosh Pandey

GitHub: @ashutoshpandey18

Email: ashutoshpandey23june2005@gmail.com