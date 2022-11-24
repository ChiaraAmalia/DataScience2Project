import pandas as pd
import matplotlib.pyplot as plt
import os
import math

dirname = os.path.dirname(__file__)

dataset = pd.read_csv(dirname+"/../out.csv")
dataset['date'] = pd.to_datetime(dataset['date'])
dataset.set_index('date')


#dataset.info()
pre_clustering1 = dataset.loc[(dataset['PM25'].notnull()) & (dataset['PM10'].notnull())]
clustering1 = pre_clustering1.iloc[:,[8,9]].values
print(clustering1.shape)
from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    km.fit(clustering1)
    wcss.append(km.inertia_)

plt.figure(figsize=(20,8))
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method', fontsize = 20)
plt.xlabel('No. of Clusters')
plt.ylabel('wcss')
plt.show()

#pmAverageStation = datasetStation28079055['PM10'].resample('10d').mean()
#pmAverageStation.plot.line(x='date',y='PM25')
#plt.show()
#pmAverage = dataset['PM25'].resample('5d')
#pmAverage.plot.line(x='date',y='PM25')
#print(pmAverage)
#dataset.plot.line(x='date',y='PM25')
#plt.show()

