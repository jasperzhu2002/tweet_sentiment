import matplotlib.pyplot as plt
import pandas as pd
from SortData import sortData
from Scrape import scrape

tweets = scrape('VitalikButerin', 100)
data = sortData(tweets, 'VitalikButerin', 'ether|Ether')

# groups by day
# data.index = pd.to_datetime(data.index)
data = data.groupby(pd.Grouper(freq = '3M')).mean()

#graphs data
plt.plot(data.index, data['Score'])
plt.show()