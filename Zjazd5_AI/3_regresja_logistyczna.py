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

from sklearn.linear_model import LogisticRegression   #regresja jest tu
from sklearn.model_selection import train_test_split   #klasa jest tu
from sklearn.metrics import confusion_matrix

df.to_csv('dane\\cukrzyca.csv', index=False)

X = df.iloc[: , :-1]
y = df.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame( confusion_matrix(y_test, model.predict(X_test) ) ))

print('Zmiana danych')
print(df.outcome.value_counts())
df1 = df.query("outcome==0").sample(n=500)
df2 = df.query("outcome==1").sample(n=500)
df3 = pd.concat([df1, df2])

X = df3.iloc[: , :-1]
y = df3.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame( confusion_matrix(y_test, model.predict(X_test) ) ))