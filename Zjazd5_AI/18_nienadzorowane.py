import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dane\\Mall_Customers.csv')
print(df.describe().T.to_string())

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

model = KMeans()
labels = model.fit_predict(X)
centroids = model.cluster_centers_

print(labels)
print(centroids)

plot_df = pd.DataFrame(X, columns=['Annual Income (k$)', 'Spending Score (1-100)'])
plot_df['Cluster'] = labels
print(plot_df)
palette = sns.color_palette("tab10", 8)
sns.scatterplot(data=plot_df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette=palette, s=60)
plt.scatter(centroids[:,0], centroids[:,1], s=200, c='black', marker='X', label='Centroidy')
plt.show()

