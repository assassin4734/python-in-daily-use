import pandas as pd


df = pd.DataFrame()
df.insert(loc=0, value=[0,1,2], allow_duplicates=True, column='V28')
print(df)