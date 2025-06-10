Stock Analysis Chatbot

This project presents a Stock Analysis Chatbot built using OpenAI’s GPT-3.5 model and the Yahoo Finance API. It enables users to retrieve real-time stock information and perform technical analysis through a simple, conversational interface. The chatbot is designed to help both novice and experienced investors gain quick access to stock prices, trends, and key indicators like SMA, EMA, and RSI.

Features
	•	Natural Language Querying
    Users can ask questions in plain English, such as “What’s the latest price of Apple?” or “Show me the RSI for Zomato.”
	•	Real-Time Stock Data
    Stock data is retrieved using the Yahoo Finance API, ensuring up-to-date information.
	•	Technical Analysis Tools
	  •	SMA (Simple Moving Average)
	  •	EMA (Exponential Moving Average)
	  •	RSI (Relative Strength Index)
	•	Graphical Plots of Stock Prices
	•	Graphical Output
    Users can view stock trends through generated plots, aiding visual analysis.

Tech Stack
	•	Language: Python
	•	NLP Engine: OpenAI GPT-3.5
	•	Financial Data Source: Yahoo Finance API (via yfinance)
	•	Frontend Interface: Streamlit
	•	Visualization: Matplotlib, Plotly

How It Works
	•	Streamlit Frontend: Provides a user-friendly input box for entering stock-related queries.
	•	GPT-3.5 Model: Parses the user’s natural language input and identifies intent.
	•	Backend Functions: Depending on the intent, specific Python functions are triggered to retrieve and analyze stock data.
	•	Result Display: The chatbot returns the results in text and graphical formats.
