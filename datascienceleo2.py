import pandas as pd
import matplotlib.pyplot as plt
import os
import math
from sklearn.preprocessing import StandardScaler
#import h5py
#f = h5py.File('mytestfile.hdf5', 'r')

dirname = os.path.dirname(__file__)

dataset = pd.read_csv(dirname+"/../out.csv")
dataset['date'] = pd.to_datetime(dataset['date'])
dataset.set_index('date')

#NO_2,PM10
#
dataset.info()
pre_clustering1 = dataset.loc[(dataset['NO_2'].notnull()) & (dataset['PM10'].notnull())]
clustering1 = pre_clustering1.iloc[:,[6,8]].values
scaler = StandardScaler()
scaler.fit(clustering1)
StandardScaler()
clustering1 = scaler.transform(clustering1)

print(clustering1.shape)
from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    km.fit(clustering1)
    wcss.append(km.inertia_)

#plt.figure(figsize=(20,8))
#plt.plot(range(1, 11), wcss)
#plt.title('The Elbow Method', fontsize = 20)
#plt.xlabel('No. of Clusters')
#plt.ylabel('wcss')
#plt.show()

km = KMeans(n_clusters = 4, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_means = km.fit_predict(clustering1)

plt.figure(figsize=(15,8))
plt.scatter(clustering1[y_means == 0, 0], clustering1[y_means == 0, 1], s = 100, c = 'pink', label = 'miser')
plt.scatter(clustering1[y_means == 1, 0], clustering1[y_means == 1, 1], s = 100, c = 'yellow', label = 'general')
plt.scatter(clustering1[y_means == 2, 0], clustering1[y_means == 2, 1], s = 100, c = 'cyan', label = 'target')
plt.scatter(clustering1[y_means == 3, 0], clustering1[y_means == 3, 1], s = 100, c = 'magenta', label = 'spendthrift')
plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:, 1], s = 50, c = 'blue' , label = 'centroid')

plt.title('K Means Clustering', fontsize = 20)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()

#pmAverageStation = datasetStation28079055['PM10'].resample('10d').mean()
#pmAverageStation.plot.line(x='date',y='PM25')
#plt.show()
#pmAverage = dataset['PM25'].resample('5d')
#pmAverage.plot.line(x='date',y='PM25')
#print(pmAverage)
#dataset.plot.line(x='date',y='PM25')
#plt.show()

