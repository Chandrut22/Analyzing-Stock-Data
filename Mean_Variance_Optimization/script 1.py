import pandas as pd
import matplotlib.pyplot as plt
from rf import return_portfolios, optimal_portfolio
import numpy as np

# 1. Load the stock data
stock_data = pd.read_csv("stock_data_weak.csv")
print(stock_data)
# 2. Find the quarterly return for each period
returns_quarterly = list(stock_data.columns[1:])

# 3. Find the expected returns 
excepted_returns = returns_quarterly.mean()

# 4. Find the covariance 
cov_quarterly = returns_quarterly.cov()

# 5. Find a set of random portfolios
random_portfolis= return_portfolis(expected_returns, cov_quartery)

# 6. Plot the set of random portfolios
df.plot.scatter(x='Volatility',y='Returns',fontsize=12)

# 7. Calculate the set of portfolios on the EF
weights,returns,risks = optimal_portfolis(returns_quartly[1:])

# 8. Plot the set of portfolios on the EF
plt.plot(risks,returns,'y-o')
plt.ylabel('Excepted Returns',fontsize=14)
plt.xlabel('Volatility (Std. Deviation)',fontsize=14)
plt.title('Efficient Frontier',fontsize=24)

# Compare the set of portfolios on the EF to the 
try:
  single_asset_std=np.sqrt(np.diagonal(cov_quarterly))
  plt.scatter(single_asset_std,expected_returns,marker='X',color='red',s=200)
except:
  pass
plt.show()
