import matplotlib.pyplot as plt
import pandas as pd
from SortData import sortData
from Scrape import scrape

people = ['VitalikButerin', 'rogerkver', 'aantonop',
          'SatoshiLite', 'APompliano', 'ErikVoorhees',
          'cz_binance', 'saylor', 'RaoulGMI', 
          'brian_armstrong', 'sandeepnailwal', 'Bitboy_Crypto',
          'CryptoHayes', '100trillionUSD']

data = []

# gets data for each twitter account
for username in people:
    tweets = scrape(username, 1000)
    data.append(sortData(tweets, username, 'ether|Ether'))

# groups by day
data = pd.concat(data)
data = data.astype({'Score': int})
data = data.groupby(pd.Grouper(freq = '3M')).mean()

#graphs data
plt.plot(data.index, data['Score'])
plt.show()