
import pandas as pd

df_movie = pd.read_csv("data/netflix1.csv")
df_director = pd.read_csv("data/netflix2.csv")

# Kolla antal rader i båda DF
df_movie.size
df_director.size

# NOTE: size är fel.

# Kolla antal unika regisorer i varje DF
df_movie['director'].nunique()
df_director['director'].nunique()

# Skapa en ny DF med enbart alla regisorer i df_director, men med alla filmer de har gjort (dvs
# flera rader per regisor). Tips: kolla att antal unika regisörer är samma som i df_director. Behåll
# alla kolumner i båda df. Kalla den nya för df_a.

df_dir = df_movie[['director', 'title']]

df_movie_update = df_dir.dropna()

# NOTE: Detta stämmer inte nu när namnen på DFs är rätt.

# Skapa en motsvarande DF med alla regisörer i df_movies som börjar på bokstaven A i förnamn. Kalla den df_b.


# Skapa en tredje DF (df_c) med alla regisörer som är med i både df_a och df_b.


# Hur många regisörer är med i df_b men inte i df_c?




