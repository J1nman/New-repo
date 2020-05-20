
import pandas as pd

df_director = pd.read_csv("data/netflix1.csv")
df_movies = pd.read_csv("data/netflix2.csv")



# Kolla antal rader i båda DF
df_director.size
df_movies.size

# Kolla antal unika regisorer i varje DF

df_director['director'].nunique()
df_movies['director'].nunique()

# Skapa en ny DF med enbart alla regisorer i df_director, men med alla filmer de har gjort (dvs
# flera rader per regisor). Tips: kolla att antal unika regisörer är samma som i df_director.

df_dir = df_director[['director', 'title']]
del df_movies['age']
df_dir = pd.merge(df_dir, df_movies)
df_dirmov = df_dir.dropna()


