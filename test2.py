import numpy as np
import pandas as pd

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