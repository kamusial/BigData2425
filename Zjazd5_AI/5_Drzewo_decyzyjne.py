import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('dane\\iris.csv')
print(df['class'].value_counts())

species = {
    'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2
}
df['class_value'] = df['class'].map(species)
print(df)
sample = [5.6, 3.2, 5.2, 1.45]

sns.scatterplot(data=df, x='sepallength', y='sepalwidth', hue='class')
plt.scatter(5.6, 3.2, c='r')
plt.show()

sns.scatterplot(data=df, x='petallength', y='petalwidth', hue='class')
plt.scatter(5.2, 1.45, c='r')
plt.show()

print('Klasyfikator Decission Tree')
X = df.iloc[:, 0:4]
y = df.class_value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=5, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, class_weight=None, ccp_alpha=0.0)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

#granice decyzyjne
# from mlxtend.plotting import plot_decision_regions
# plot_decision_regions(X.values, y.values, model)
# plt.show()

print(pd.DataFrame(model.feature_importances_, X.columns))
