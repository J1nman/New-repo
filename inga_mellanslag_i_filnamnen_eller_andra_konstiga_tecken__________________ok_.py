import os
import pandas as pd
​
path = 'D:\python'
​
df_t = pd.read_pickle(os.path.join(path, '...'))
​
df_l = pd.read_csv(os.path.join(path, '...'), sep=';')
df_l = df_l.dropna(subset=['...'])
​
df_t_b = pd.read_csv(os.path.join(path, '...'), sep=';')
​
# All duplicates are equal in diagnosis
df_l = df_l.drop_duplicates(subset=['...']) # deletes duplicates
​
# Rename before merge.
df_t['...'] = df_t.Term
df_l['...'] = df_l.Term

df_t_b.rename(columns={'...':'...'}, inplace=True)

df_t['...'] = df_t['...']  # Creates another column with same values
df_l['...'] = df_l['...']
df_t_b['...'] = df_t_b['...']

# Remove ext from filenames


df = df.sort_values(by='...')

# Merge
df_disagree = pd.merge(left=df[['...', '...', '...',]], # puts 2 DataFrame into 1 thats written in "how", sorted by "on"
              right=df2[['...', '...',]],
              how='left',
              on='filename')
​
# Remove all text in the columns '...' and '...' that contains ..., i.e.
# the columns should only contain the strings '...' and 'No ...'.

df['...'] = df['...'].str.replace('...', '') # to replace txt in chosen column name


pd.crosstab(df.L,df.T,margins=True)
# Use pandas crosstab function to see in how many cases ... and ... disagree.

(T was true where L was false in 35 cases)
df = df.sort_values(by=['...', '...'], ascending=[True, False]) # Sorted True value with False value in the other column in my case

boollista = (df.L == 'P') & (df.T == 'No P') # another solution for sorting
df = df[boollista]
df_d = df_d[0:35]

df_d.to_csv('D:...\name', sep=',')
