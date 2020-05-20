# Kolla att alla filnamn stämmer överens i båda filerna.

import os
import pandas as pd

# Här får du byta path så det passar din dator.
path = 'D:/PNI_AI/Multipathologist/df_multi.pkl'
path_kiuas = 'D:/PNI_AI/Multipathologist/PNI_to_Cyto.txt'

# Läs in filerna.
df = pd.read_pickle(path)
df_c = pd.read_csv(path_kiuas)
type(df_c)  # En Dataframe med enbart en kolumn.

# Du kan titta på innehållet genom att trycka på glasögongen 'Show  variables' och klicka på 'View DataFrame'.
# Eller tex:
df.head()

# I DataFrame df så finns det en kolumn som heter 'filename'. Tanken är nu att verifiera att alla filnamnen
# i den kolumnen finns med i den andra DataFrame df_c. Varje rad i df_c är en textsträng och den innehåller
# ett filnamn. Det gäller att matcha den delen av strängen med namnen i df.filename.

filnamn = df.filename  # Plocka ut enbart filnamnskolumnen
filnamn  # printar alla filanmn
len(filnamn)  # Kollar antalet filnamn

filnamn2 = df_c['total 26216472']
len(filnamn2)

# Nu får du lösa problemet att plocka ut filnamnsdelen ut filnamn2. Detta görs lättast med list comprehension
# tillsammans med funktionerna split() och rsplit(). Googla. Här är ett exempel:

a = ['Peter', 'Svante', 'Tony']
b = ['Peter.23', 'Svante.dfjkl2']

ny_b = [text.split(".")[0] for text in b]

# Sedan är det bara att kolla att alla är med tex genom att gör om listorna till set och kolla på intersection.
finns_i_alla = set(a).intersection(set(ny_b))
len(a) == len(finns_i_alla)  # False, det vill säga alla namn i a finns inte i b (eller tvärt om).


# Gör samma sak med filnamnen genom att hitta saker att splitta på som funkar för alla rader (detektivarbete).

