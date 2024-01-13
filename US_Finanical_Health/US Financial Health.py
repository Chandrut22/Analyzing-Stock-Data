import pandas as pd
import pandas_datareader.data as web
import pandas_datareader.wb as wb
import numpy as np
from datetime import datetime

gold_prices = pd.read_csv('gold_prices.csv')
crude_oil_prices = pd.read_csv('crude_oil_prices.csv')

print(gold_prices)
print(crude_oil_prices)

start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)

nasdaq_data = web.DataReader( 'NASDAQ100', 'fred', start, end)
sap_data = web.DataReader('SP500', 'fred', start, end)

print(nasdaq_data)
print(sap_data)

gdp_data = wb.download(indicator = 'NY .GDP .MKTP .CD', country= ['US'], start =start, end=end)
export_data = wb.download(indicator = 'NE .EXP .GNFS. CN',countory = ['US'], start =start, end=end)

print(gdp_data)
print(export_data)
def log_return(prices):
  return np.log(prices / prices.shift(1))

gold_returns = log_return(gold_prices['Gold_price'])

crude_oil_return = log_return(crudeoil_prices['Crude_Oil_Price'])

nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])

sap_returns = log_return(sap_data['SP500'])

gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])

export_returns = log_return(expport_data['NE.EXP.GNFS.CN'])
