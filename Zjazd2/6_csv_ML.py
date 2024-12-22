import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'files\otodom.csv')
print(df)
print(df.describe().T.to_string())   # opis danych
print(df.iloc[  3:10  ,  1:4  ])  # wycinam wiersze i kolumny
sns.heatmap(df.iloc[:, 1:].corr(), annot=True)
plt.show()
