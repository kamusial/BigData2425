import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
import pandas as pd

X, y = make_circles(n_samples=100, factor=0.6, noise=0.1)
print(X)
print(y)
plt.scatter(X[:, 0], X[:, 1]   , c=y  )
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=0)


from sklearn.linear_model import LogisticRegression
print('Regresja logistyczna')
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))