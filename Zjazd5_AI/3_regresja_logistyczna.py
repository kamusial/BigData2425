import pandas as pd
import numpy as np

df = pd.read_csv('dane\diabetes.csv')
print(df.describe().T.to_string())

# wpisać wartosci srednie (bez zer) tam, gdzie 0 albo brak wartości

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
       # usunąć zera
       df[col].replace(0, np.nan, inplace=True)
       # policzyć średnia
       mean_ = df[col].mean()
       # wpisać średnia tam,gdzie brak wartości
       df[col].replace(np.nan, mean_, inplace=True)

print('Po czyszczeniu')
print(df.describe().T.to_string())

df.to_csv('dane\\cukrzyca.csv', index=False)
