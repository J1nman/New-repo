import os

import pandas as pd
from Tools.scripts.make_ctype import values
from numpy import insert

airports = pd.read_csv('airports.csv')
airport_freq = pd.read_csv('airport-frequencies.csv')
runways = pd.read_csv('runways.csv')

airports[airports.ident == 'KLAX'].id
airports.type.unique()

airport_freq[airport_freq.airport_ident == 'KLAX'].sort_values('type')
airports[~airports.type.isin(['heliport', 'balloonport'])]

airports.groupby(['iso_country', 'type']).size()

airports.groupby(['iso_country', 'type']).size().to_frame('size').reset_index().sort_values(['iso_country', 'size'],
                                                                                            ascending=[True, False])

airports[airports.iso_country == 'US'].groupby('type').filter(lambda g: len(g) > 1000).groupby('type').size().sort_values(ascending=False)



runways.agg({'length_ft': ['min', 'max', 'mean', 'median']})

df = airport_freq.merge(airports[airports.ident == 'KLAX'][['id']], left_on='airport_ref',
                   right_on='id',
                   how='inner')[['airport_ident', 'type', 'description', 'frequency_mhz']]

df2 = pd.concat([airports[airports.ident == 'KLAX'][['name', 'municipality']], airports[airports.ident == 'KLGB'][['name', 'municipality']]])


df1 = pd.DataFrame({'id': [1, 2], 'name': ['Harry Potter', 'Ron Weasley']})
df2 = pd.DataFrame({'id': [3], 'name': ['Hermione Granger']})
df3 = pd.concat([df1, df2]).reset_index(drop=True)

airports.loc[airports['ident'] == 'KLAX', 'home_link'] = 'http://www.lawa.org/welcomelax.aspx'
airports[airports.ident.isin(['KLAX'])]


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser1[~ser1.isin(ser2)]

import numpy as np
ser = pd.Series(np.random.normal(10, 5, 25))
np.percentile(ser, q=[0, 25, 50, 75, 100])

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser.value_counts()

ser = pd.Series(np.random.randint(1, 10, 35))
df_ser = pd.DataFrame(ser.values.reshape(7,5))