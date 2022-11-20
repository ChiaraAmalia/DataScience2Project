import pandas as pd

'''path = r"C:\\Users\\pc\\Desktop\\Università\\Data science\\Progetti\\ProgettoPython\\Dataset\\archive (1)\\csvs_per_year\\csvs_per_year\\"
madrid2018 = pd.read_csv(path+"madrid_2018.csv")
madrid2011 = pd.read_csv(path+"madrid_2011.csv")
madrid2008 = pd.read_csv(path+"madrid_2008.csv")
print("caricamento ok")
print(madrid2018['CH4'].isna().sum())
madrid2018.drop(columns=['CH4', 'NOx'],inplace=True)
print(madrid2018.head(0))
print(madrid2011.head(0))
completeDataset = pd.concat([madrid2011,madrid2018])
print(len(completeDataset.index))
madrid2008['pippo'] = 5
print(madrid2008.head())
new = madrid2008.iloc[:, [14,0,1,2,3,4,5,6,7,8,9,10,11,12,13]]
print(madrid2008.head())
print(new.head())
'''

df = pd.DataFrame({'ID':['1', '2', '3'], 'col 1': [0, 2, 3], 'col 2':[1, 4, 5]})
mylist = ['a', 'b', 'c', 'd', 'e', 'f']

def get_sublist(sta,end):
    return mylist[sta:end+1]

df['col_3'] = df.apply(lambda x: print('va bene') if x['col 1'] > x['col 2'] else print('pippo'), axis=1)
print(df[:0])