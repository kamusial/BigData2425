import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('dane\\weight-height.csv')
print(df.head(10))
print(df.Gender.value_counts())
df.Height *= 2.54
df.Weight /= 2.2
print(f'Po zmianie jednostek: \n{df.head(10)}')

# niezależne 2 kolumny - gender i height. Wynik weight.
# wszyscy
# plt.hist(df.Weight, bins=50)
# plt.show()

# osobno panie i panowie
# plt.hist(df.query("Gender=='Male'").Weight, bins=50)
# plt.hist(df.query("Gender=='Female'").Weight, bins=50)
# plt.show()

df = pd.get_dummies(df)   # usuwam dane nienumeryczne, zamienia na numeryczne
print(df.head())
del df['Gender_Male']    # usuwa kolumne
print(df.head())
df.rename(columns={'Gender_Female': 'Gender'}, inplace=True)   # wykonaj w locie
print(df.head())

# dane na stole
# Gender  0 - mezczyzna,     1 - kobieta
model = LinearRegression()
model.fit( df[['Height', 'Gender']]       , df['Weight']      )

print(f'Współczynnik kierunkowy: {model.coef_}\nWyraz wolny: {model.intercept_}')

print(f'waga = wzrost * 1.07 - plec * 8.8 - 102.5')

# sprawdzenie
print(model.predict([[192, 0], [167, 1], [80, 1]] ))
