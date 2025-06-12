# Stock Analysis Chatbot

This project features a conversational Stock Analysis Chatbot built using OpenAI’s GPT-3.5 model and the Yahoo Finance API. It enables users to retrieve real-time stock data and perform technical analysis through a natural language interface. The chatbot is designed to assist both beginners and seasoned investors in accessing key stock metrics and visual trends quickly and efficiently.

## Features

- **Natural Language Querying**  
  Ask questions like “What’s the latest price of Apple?” or “Show me the RSI for Zomato.”

- **Real-Time Stock Data**  
  Data is fetched using the Yahoo Finance API via the `yfinance` library.

- **Technical Analysis Tools**  
  - SMA (Simple Moving Average)  
  - EMA (Exponential Moving Average)  
  - RSI (Relative Strength Index)

- **Graphical Output**  
  Generates plots to visualize stock price trends and indicators.

## Tech Stack

- **Language**: Python  
- **NLP Engine**: OpenAI GPT-3.5  
- **Financial Data Source**: Yahoo Finance API (`yfinance`)  
- **Frontend Interface**: Streamlit  
- **Visualization**: Matplotlib, Plotly

## How It Works

1. **Streamlit Interface**  
   Users interact with a simple web interface to input stock-related queries.

2. **GPT-3.5 Integration**  
   The model interprets natural language input and extracts the user’s intent.

3. **Backend Processing**  
   The chatbot triggers appropriate functions to fetch stock data and compute technical indicators.

4. **Results Display**  
   The chatbot returns answers in both text and graphical formats for clarity and ease of interpretation.

## Setup Instructions

1. Clone the repository.
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
