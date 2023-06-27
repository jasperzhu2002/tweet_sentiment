import matplotlib.pyplot as plt
import pandas as pd
from SortData import sortData
from Scrape import scrape
import glob
import os

people = ['VitalikButerin', 'rogerkver', 'aantonop',
          'SatoshiLite', 'APompliano', 'ErikVoorhees',
          'cz_binance', 'saylor', 'RaoulGMI', 
          'brian_armstrong', 'sandeepnailwal', 'Bitboy_Crypto',
          'CryptoHayes', '100trillionUSD', 'BarrySilbert',
          'TimDraper', 'elonmusk', 'cbventures',
          'CryptoCred', 'redxbt', 'loomdart', 
          'Pentosh1', 'CoinDeskMarkets', 'Cointelegraph',
          'cryptonews', 'coincultureau', 'ConsenSys',
          'PanteraCapital', 'paradigm', 'protocollabs']
test = ['RaoulGMI']
currDir = os.getcwd()
path = currDir + '/data'
files = glob.glob(os.path.join(path, "*.csv"))

print(path)

data = []

# gets data for each twitter account
# for username in people:
#     tweets = scrape(username, 5000)
#     data.append(sortData(tweets, username, 'ether|Ether|Crypto|crypto|Bitcoin|bitcoin|bit|Bit|blockchain|coin|Coin|market|Market|exchange|Exchange'))

for f in files:
    print(f.split("/")[-1])
    df = pd.read_csv(f)
    df = df.drop(df.columns[0], axis=1)
    username = f.split("/")[-1].split('_')[0]
    data.append(sortData(df, username, 'ether|Ether|Crypto|crypto|Bitcoin|bitcoin|bit|Bit|blockchain|coin|Coin|market|Market|exchange|Exchange'))

# groups by day and calculate moving averagep
data = pd.concat(data)
data.index = pd.to_datetime(data.index)
data = data.astype({'Score': int})
print(data)
data = data.groupby(pd.Grouper(freq = '2D')).mean()
data[ 'rolling_avg' ] = data.Score.rolling(5).mean()

#graphs data
plt.plot(data.index, data['Score'], label='Per Period')
plt.plot(data.index, data['rolling_avg'], label='Rolling Avg')
plt.show()