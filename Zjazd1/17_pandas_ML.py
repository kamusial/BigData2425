import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

sns.histplot(df.query("Gender=='Male'").Weight)
sns.histplot(df.query("Gender=='Female'").Weight)
plt.show()