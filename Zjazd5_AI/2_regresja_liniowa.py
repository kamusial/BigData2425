import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('dane\\otodom.csv')
print(df)

print(df.describe().T.to_string())   # T- zamiana wiersze z kolumnami

sns.heatmap(df.iloc[:, 2:].corr(), annot=True)   # omijamy kolumnę ID
plt.show()

sns.histplot(df.price)
plt.show()
plt.scatter(df.space, df.price)
plt.show()

q3 = df.describe().T.loc['price', '75%']
print(q3)

df1 = df[df.price <= q3]
plt.hist(df1.price, bins=50)
plt.show()

X = df1.iloc[:, 2:]
y = df1.price
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(model.coef_ , X.columns))

print('drzewo decyzyjne')
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))