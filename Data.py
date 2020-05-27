import pandas as pd
import pickle
df = pd.read_pickle('database_20190130.pkl')
df2 = df[['slide', 'filename']]
na_free = df2.dropna()
only_na = df2[~df2.index.isin(na_free.index)]
na_free = na_free.slide.value_counts()
na_free = na_free.value_counts()
only_na
na_free[0] = 126450  # add nan in only_na as 0

df_d = df
df_d.drop_duplicates(subset='slide', keep='first')
df_d = df_d.groupby(['subject']).size().reset_index(name='counts')
df_d = df_d.sort_values(by=['counts'], ascending=False)
df_data = df_d
counts2 = df_data['counts'].value_counts()
counts2 = pd.Series(counts2.index, index=counts2.values)
counts2