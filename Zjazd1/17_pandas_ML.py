import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


df = pd.read_csv('weight-height.csv')
# print(type(df))
# print(df)
print(df.head(3))
print(df.Gender.value_counts())
df.Height *= 2.54
df.Weight /= 2.2
print(df.head(3))

# plt.hist(df.Weight, bins=30)
# plt.show()
#
# sns.histplot(df.Weight)
# plt.show()

# sns.histplot(df.query("Gender=='Male'").Weight)
# sns.histplot(df.query("Gender=='Female'").Weight)
# plt.show()

print(df.describe())

df = pd.get_dummies(df)  #zmiana na dane numeryczne
print(df.head(3))
del df['Gender_Male']
print(df.head(3))
df.rename(columns={'Gender_Female': "Gender"}, inplace=True)
print(df.head(3))
# 0 - facet, 1 - kobieta

model = LinearRegression()
model.fit(df[['Height', 'Gender']],  df['Weight'] )
print(f'Wspolczynnik kierunkowy: {model.coef_}')
print(f'Wyraz wolny: {model.intercept_}')
print('wzór: Height * ',model.coef_[0], '+ Gender * ',model.coef_[1], '+ ',model.intercept_)