
import pandas as pd

df_movie = pd.read_csv("data/netflix1.csv")
df_director = pd.read_csv("data/netflix2.csv")



# Kolla antal rader i båda DF
import numpy as np

len(df_director)
len(df_movie)

# Kolla antal unika regisorer i varje DF

df_director['director'].nunique()
df_movie['director'].nunique()

# Skapa en ny DF med enbart alla regisorer i df_director, men med alla filmer de har gjort (dvs
# flera rader per regisor). Tips: kolla att antal unika regisörer är samma som i df_director. Behåll
# alla kolumner i båda df. Kalla den nya för df_a.


df_a = pd.merge(df_director, df_movie, how='left', on='director')
df_a = df_a[df_a['type'] != 'TV Show']

# snyggt!

# Skapa en motsvarande DF med alla regisörer i df_movies som börjar på bokstaven A i förnamn. Kalla den df_b.


df1 = df_movie.dropna()
df1 = df1[df1.director.str.startswith('A')]
df_b = pd.merge(df_director, df1, how='right', on='director')
df_b = df_b[df_b['type'] != 'TV Show']


# Skapa en tredje DF (df_c) med alla regisörer som är med i både df_a och df_b.

df = [df_a, df_b]
df_c = pd.concat(df)
df_c = df_c[['director']]
df_c = df_c.drop_duplicates()

# Rätt, men om man vill ha med alla kolumnerna så kan man göra:
df2 = pd.merge(df_a, df_b, how='outer', on='director')

len(df_c.director.unique()) == len(df2.director.unique())
# Hur många regisörer är med i df_c men inte i df_b?

df_d = df_b[['director']]
df_d = df_d.drop_duplicates()
df_d = pd.concat([df_d, df_c]).drop_duplicates(keep=False)


# Funkar! :)

# Med df_a, behåll enbart den film som har högst rating per regisör.

df_e = df_a.dropna()
df_e['duration'] = df_e['duration'].str.replace(' min', '')
df_e['duration'] = pd.to_numeric(df_e.duration, errors='coerce')

df_e = df_e.loc[df_e.groupby('director')['duration'].idxmax()].sort_values('duration', ascending=False)
df_e = df_e.sort_values(by=['director'])




# Med df_a, skapa en ny DF som har en kolumn medelvärde av rating per regisör (dvs en rad per regisör).

df_f = df_a
df_f = df_f[df_f['type'] != 'TV Show']

df_f = df_f.dropna()
df_f['duration'] = df_f['duration'].str.replace(' min', '')
df_f['duration'] = pd.to_numeric(df_f.duration, errors='coerce')

df_f = df_f.groupby('director', as_index=False)['duration'].mean()
df_f = df_f.sort_values(by=['director'])


len(df_f.director.unique()) == len(df_e.director.unique())

# hur många filmer/Tv Shows har varje regissör gjort
df_g = df_movie
df_g = df_g.groupby(['director']).size().reset_index(name='counts')
df_g = df_g.sort_values(by=['counts'], ascending=False)


# hur många regissörer har gjort hur många filmer/Tv Shows

df_g.counts.value_counts()

# alla filmer från de regisörer som gjort exakt 2 filmer
df_h = df_movie[['director', 'title']]
counts = df_h['director'].value_counts()
df_h = df_h[df_h['director'].isin(counts.index[counts == 2])]
df_h = df_h.sort_values(by=['director'], ascending=True)