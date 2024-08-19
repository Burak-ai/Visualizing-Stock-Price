import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

stock_data = yf.download('NVDA', start='2023-01-01', end='2024-08-17')

plt.figure(figsize=(12, 6))
plt.plot(stock_data["Close"], label="Closing Price")
plt.title("NVIDIA")
plt.xlabel("Data")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()
