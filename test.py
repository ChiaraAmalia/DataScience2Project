from scipy import stats
import numpy as np
x = np.arange(20)
pippo = stats.trim_mean(x, 0.1)
print(pippo)
VOTI = [np.nan, 7, np.nan, 4, 4, np.nan, 6, np.nan, 7, 6,np.nan]
VOTI.sort()
ciccio = stats.trim_mean(VOTI,0.1)
print('simone guarda qui')
print(ciccio)

import pandas as pd

#initialize a dataframe
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

#convert pandas dataframe to numpy array
arr = df.to_numpy()

print('\nNumpy Array\n----------\n', arr)
print('\nNumpy Array Datatype :', arr.dtype)
a_list = list(arr)
print(a_list)
print(type(VOTI))
flat_list = []
for sublist in a_list:
    for item in sublist:
        flat_list.append(item)
print(flat_list)
flat_list2 = [item for sublist in a_list for item in sublist]
print(flat_list2)
ciccio2 = stats.trim_mean(flat_list2,0.1)
print(ciccio2)

# Test stazioni
m8 = [28079001, 28079003, 28079027, 28079026, 28079025, 28079023, 28079022, 28079021, 28079036, 28079019, 28079018,28079016,28079099, 28079014, 28079040, 28079012, 28079038, 28079009, 28079007, 28079006, 28079004, 28079039, 28079011, 28079024, 28079008, 28079015]
s = [28079004, 28079008, 28079011, 28079016, 28079017, 28079018, 28079024, 28079027, 28079035, 28079036, 28079038, 28079039, 28079040, 28079047, 28079048, 28079049, 28079050, 28079054, 28079055, 28079056, 28079057, 28079058, 28079059, 28079060]

for x in m8:
    if(not s.__contains__(x)):
        print(x)