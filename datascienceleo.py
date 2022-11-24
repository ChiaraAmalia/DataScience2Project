import pandas as pd
import matplotlib.pyplot as plt
import os

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, '../')

dataset = pd.read_csv(path+"MadridAir.csv")
dataset['date'] = pd.to_datetime(dataset['date'])
dataset.set_index('date')

dataset1 = pd.read_csv(path+"/Code/DataSet/stations.csv")


def InfoStation(station:int,dataset:any):
    datasetStation = dataset[dataset.station == station]
    datasetStation.set_index('date', inplace=True)
    print(station)
    datasetStation.info()
    return datasetStation


InfoStation(28079004,dataset)
InfoStation(28079008,dataset)
InfoStation(28079011,dataset)
InfoStation(28079016,dataset)
InfoStation(28079017,dataset)
InfoStation(28079018,dataset)
InfoStation(28079024,dataset)
InfoStation(28079027,dataset)
InfoStation(28079035,dataset)
InfoStation(28079036,dataset)
InfoStation(28079038,dataset)
InfoStation(28079039,dataset)
InfoStation(28079040,dataset)
InfoStation(28079047,dataset)
InfoStation(28079048,dataset)
InfoStation(28079049,dataset)
InfoStation(28079050,dataset)
InfoStation(28079054,dataset)
InfoStation(28079055,dataset)
InfoStation(28079056,dataset)
InfoStation(28079057,dataset)
InfoStation(28079058,dataset)
InfoStation(28079059,dataset)
InfoStation(28079060,dataset)

#pmAverageStation = datasetStation28079055['PM10'].resample('10d').mean()
#pmAverageStation.plot.line(x='date',y='PM25')
#plt.show()
#pmAverage = dataset['PM25'].resample('5d')
#pmAverage.plot.line(x='date',y='PM25')
#print(pmAverage)
#dataset.plot.line(x='date',y='PM25')
#plt.show()

