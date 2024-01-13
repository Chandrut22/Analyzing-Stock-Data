from utils import *

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]


print('The value formatted as a percentage is ' , [ display_as_percentage(a) for a in amazon_prices ])
print('The value formatted as a percentage is ' , [ display_as_percentage(a) for a in ebay_prices ])

returns =[]

def get_returns(prices):
  for i in range (0,len(prices)-1):
    start_prices = prices[i]
    end_prices = prices[i +1]
    returns = calculate_log_return (start_prices,end_prices)
  return returns

amazon_returns = get_returns(amazon_prices)

ebay_returns = get_returns(ebay_prices)

print('Amazon returns is:',display_as_percentage(amazon_returns))
print('Ebay returns is:',display_as_percentage(ebay_returns))

sum_amazon_returns = sum(amazon_prices)
sum_ebay_returns = sum(ebay_prices)

print('Amazon returns is:',display_as_percentage(sum_amazon_returns))
print('Ebay returns is:',display_as_percentage(sum_ebay_returns))

print([calculate_variance(a) for a in amazon_returns ])
print(calculate_variance(sum_ebay_returns))
