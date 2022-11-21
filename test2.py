import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

x = np.arange(20)
print(x)
VOTI = [1, 10, 10, 10,10, 10, 10, 9, 0, 100] 
perc = 0.20        #  Percentuale da troncare
 
N   = len(VOTI)    #  10, Numero di elementi
pN  = int(perc*N)  #   2, Percentuale di N (da troncare)
pN2 = pN//2        #   1, Metà della percentuale di N
NN  = N-pN 
VOTI.sort()
 
totale=0
for i in range(pN2,N-pN2):
    totale += VOTI[i]
 
media = totale/NN
print(media)
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
new = df[['col2']]
print(new.head())

# pezzo tolto allMadrid['BEN'].mean(),allMadrid['CO'].mean(),allMadrid['EBE'].mean(),allMadrid['NMHC'].mean(),allMadrid['NO'].mean(),allMadrid['NO_2'].mean(),allMadrid['O_3'].mean(), ,allMadrid['SO_2'].mean(),allMadrid['TCH'].mean(),allMadrid['TOL'].mean()



plotdata = pd.DataFrame({
    "pies_2018":[40, 12, 10, 26, 36],
    "pies_2019":[19, 8, 30, 21, 38],
    "pies_2020":[10, 10, 42, 17, 37]
    }, 
    index=["Dad", "Mam", "Bro", "Sis", "Me"]
)

# Adding the stacked=True option to plot() 
# creates a stacked bar plot
plotdata.plot(kind='bar', stacked=True)
plt.title("Total Pie Consumption")
plt.xlabel("Family Member")
plt.ylabel("Pies Consumed")

plt.show()