import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


stock_symbol = "AAPL"  
start_date = "2019-01-01"
end_date = "2024-01-01"

data = yf.download(stock_symbol, start=start_date, end=end_date)

print(data.head())

plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label=f'{stock_symbol} Close Price')
plt.title(f'{stock_symbol} Stock Price - Time Series')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.show()
