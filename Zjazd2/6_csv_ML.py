import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from functions import prepare_file_name
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r'files\otodom.csv')
print(df)
print(df.describe().T.to_string())   # opis danych
print(df.iloc[  3:10  ,  1:4  ])  # wycinam wiersze i kolumny
# sns.heatmap(df.iloc[:, 1:].corr(), annot=True)
# plt.show()
#
# plt.hist(df.price, bins=30)
# plt.hist(df.price, bins=20)
# plt.show()
#
# sns.histplot(df.price, bins=50)
# sns.histplot(df.price)
# plt.savefig(r'charts\wykres'+prepare_file_name()+'.png')
# plt.savefig(r'charts\wykres.pdf')
# plt.show()

q1 = df.describe().T.loc['price', '25%']
q3 = df.describe().T.loc['price', '75%']
print(f'cena na koncu q1 to: {q1}')
print(f'cena na koncu q3 to: {q3}')

df1 = df[df.price <= q3]
sns.histplot(df1.price)
plt.show()

X = df1.iloc[:, 2:]
y = df1.price
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)
print(f'\n\n{model.score(X_test, y_test)}\n\n')
print(pd.DataFrame(model.coef_, X.columns))




