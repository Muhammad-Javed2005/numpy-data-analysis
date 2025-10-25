from data_fetch import fetch_data
from simulator import simulate_portfolios
from plotter import plot_efficient_frontier

# tickers = ['AAPL', 'MSFT', 'GOOG', 'META']
# tickers = ['TSLA', 'AMZN', 'NVDA', 'NFLX']
# tickers = ['TSLA', 'AMZN', 'NVDA']
# tickers = ['BTC-USD', 'ETH-USD', 'SOL-USD']  # Crypto
# tickers = ['SPY', 'QQQ', 'IWM']  # ETFs
# tickers = ['BTC-USD', 'LUNA1-USD', 'DOGE-USD']  # Highly volatile crypto
tickers = ['BTC-USD', 'DOGE-USD', 'LUNA1-USD']




returns = fetch_data(tickers, '2020-01-01', '2024-12-31')
results = simulate_portfolios(returns)
plot_efficient_frontier(results)


