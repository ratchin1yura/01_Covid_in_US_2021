# import numpy as np
import pandas as pd

us1 = pd.read_csv('us-counties-2021.csv', delimiter=',')

look_column = 'state'
look_text = 'Texas'
us1 = us1[us1[look_column].str.contains(look_text)]
print(f'Статистика по штату {look_text}:')
print(us1)

# print(us1.sample(10))
# print(us1[0:10])
