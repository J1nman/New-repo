
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


df_a = pd.merge(df_director, df_movie, on='director')
df_a = df_a[df_a['type'] != 'TV Show']


# NOTE: Fel. Alla regisörer är inte med från df_director. Kolla ALLTID att koden du kör ger de
# resultat du förväntar dig. Jag gör alltid det också (efter 7 år) annars blir det ofta fel.
# len(df_a.director.unique())


# Skapa en motsvarande DF med alla regisörer i df_movies som börjar på bokstaven A i förnamn. Kalla den df_b.

df_b = df_movie[df_movie['director'] == 'A&']
df_movie = df_movie.dropna()
df_b = df_movie[df_movie.director.str.startswith('A')]

# Fel. Den ska vara motsvarande, dvs alla kolumner som finns i df_a (inkl age).

# Skapa en tredje DF (df_c) med alla regisörer som är med i både df_a och df_b.

df = [df_a, df_b]
df_c = pd.concat(df)
df_c = df_c[['director']]
df_c = df_c.drop_duplicates()

# Ja, det här stämmer. bra lösning. dock tänkte jag att alla kolumnerna skulle vara kvar - var otydlig.

# Hur många regisörer är med i df_b men inte i df_c?

df_b = df_b[['director']]
df_b = df_b.drop_duplicates()

pd.concat([df_b, df_c]).drop_duplicates(keep=False)

# Det här stämmer nog inte? Eller? Tips: använd merge istället för concat.
