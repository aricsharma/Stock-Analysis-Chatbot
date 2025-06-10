import json
import openai
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf

openai.api_key = open('API_Key', 'r').read()


def get_stock_price(ticker):
    return str(yf.Ticker(ticker).history(period='1y').iloc[-1].Close)

def calculate_SMA(ticker, window):
    data = yf.Ticker(ticker).history(period='1y').Close
    return str(data.rolling(window=window).mean().iloc[-1])

def calculate_EMA(ticker, window):
    data = yf.Ticker(ticker).history(period='1y').Close
    return str(data.rolling(span=window, adjust=False).mean().iloc[-1])

def plot_stock_price(ticker):
    data = yf.Ticker(ticker).history(period='1y')
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data.Close)
    plt.title('(ticker) Stock Price Over Last Year')
    plt.xlabel('Date')
    plt.ylabel('Stock Price ($)')
    plt.grid(True)
    plt.savefig('stock.png')
    plt.close()

functions = [
    {
        'name': 'get_stock_price',
        'description': 'Gets the latest stock price given the ticker symbol of a company.',
        'parameters': {
            'type': 'object',
            'properties':{
                'ticker': {
                    'type': 'string',
                    'description': 'the stock ticker symbol for a company (for example AAPL for Apple.)'
                } 
            },
            'required': ['ticker']
        },
    },
    {
        'name': 'calculate_SMA',
        'description': 'Calculate the Simple Moving Average of a given stock and a window.',
        'parameters': {
            'type': 'object',
            'properties':{
                'ticker': {
                    'type': 'string',
                    'description': 'the stock ticker symbol for a company (for example AAPL for Apple.)'
                },
                'window':{
                    'type': 'integer',
                    'description': 'The timeframe to consider when calculating the SMA'
                } 
            },
            'required': ['ticker', 'window'],
        },
    },
    {
        'name': 'calculate_EMA',
        'description': 'Calculate the Exponential Moving Average of a given stock and a window.',
        'parameters': {
            'type': 'object',
            'properties':{
                'ticker': {
                    'type': 'string',
                    'description': 'the stock ticker symbol for a company (for example AAPL for Apple.)'
                },
                'window':{
                    'type': 'integer',
                    'description': 'The timeframe to consider when calculating the SMA'
                } 
            },
            'required': ['ticker', 'window'],
        },
    },
    {
        'name': 'plot_stock_price',
        'description': 'Plot the stock price given the ticker symbol of a company.',
        'parameters': {
            'type': 'object',
            'properties':{
                'ticker': {
                    'type': 'string',
                    'description': 'the stock ticker symbol for a company (for example AAPL for Apple.)'
                } 
            },
            'required': ['ticker']
        },
    },
]

available_functions = {
    'get_stock_price': get_stock_price,
    'calculate_SMA': calculate_SMA,
    'calculate_EMA': calculate_EMA,
    'plot_stock_price': plot_stock_price
}

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.title('Stock Analysis Chatbot Assistant')

user_input = st.text_input("Your Input: ")

if user_input:
    try:
        st.session_state['messages'].append({'role': 'user', 'content': f'{user_input}'})

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo-0613',
            messages=st.session_state['messages'],
            functions=functions,
            function_call='auto'
        ) 

        response_message = response['choices'][0]['message']

        if response_message.get('function_call'):
            function_name = response_message['function_call']['name']
            function_args = json.loads(response_message['function_call']['arguments'])
            if function_name in ['get_stock_price', 'plot_stock_price']:
                args_dict = {'ticker': function_args.get('ticker')}
            elif function_name in ['calculate_SMA', 'calculate_EMA']:
                args_dict = {'ticker': function_args.get('ticker'), 'window': function_args.get('window')}

            function_to_call = available_functions[function_name]
            function_response = function_to_call(**args_dict)

            if function_name == 'plot_stock_price':
                st.image('stock.png')

            else:
                st.session_state['messages'].append(response_message)
                st.session_state['messages'].append(
                    {
                        'role': 'function',
                        'name': function_name,
                        'content': function_response
                    }
                )
                second_response = openai.ChatCompletion.create(
                        model='gpt-3.5-turbo-0613',
                        messages=st.session_state['messages']
                    )
                st.text(second_response['choices'][0]['message']['content'])
                st.session_state['messages'].append({'role': 'assistant', 'content': second_response['choices'][0]['message']['content']})
        
        else:
            st.text(response_message['content'])
            st.session_state['messages'].append({'role': 'assistant', 'content': response_message['content']})    
    except Exception as e:
        raise e