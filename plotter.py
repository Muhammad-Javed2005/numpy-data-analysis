import matplotlib.pyplot as plt
import numpy as np

def plot_efficient_frontier(results):
    plt.figure(figsize=(12, 8))
    plt.scatter(results['volatility'], results['returns'], c=results['sharpe'], cmap='viridis')
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Volatility (Risk)')
    plt.ylabel('Expected Return')
    plt.title('Efficient Frontier')
    plt.grid(True)
    plt.show()

    

