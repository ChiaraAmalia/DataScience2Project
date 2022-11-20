import pandas as pd
import matplotlib.pyplot as plt
import os

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, '../')

dataset = pd.read_csv(path+"MadridAir.csv")
dataset['date'] = pd.to_datetime(dataset['date'])
dataset.set_index('date')
print(dataset['date'].dtypes)
pmAverage = dataset.PM25.rolling(30).mean()
pmAverage.plot.line(x='date',y='PM25')
#print(pmAverage)
dataset.plot.line(x='date',y='PM25')
plt.show()