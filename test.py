from scipy import stats
import numpy as np
x = np.arange(20)
pippo = stats.trim_mean(x, 0.1)
print(pippo)
VOTI = [3, 7, 8, 4, 4, 9, 6, 8, 7, 6]
VOTI.sort()
ciccio = stats.trim_mean(VOTI,0.1)
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