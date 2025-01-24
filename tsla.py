import yfinance as yf

# Fetch Tesla (TSLA) historical data for the past year
tsla = yf.Ticker("TSLA")
data = tsla.history(start="2023-01-01", end="2024-01-01", interval="1d")

# Save data to CSV file
data.to_csv("tsla_1yr_data.csv")
print("Data saved as tsla_1yr_data.csv")
