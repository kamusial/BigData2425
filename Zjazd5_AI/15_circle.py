import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
import pandas as pd

X, y = make_circles(n_samples=10, factor=0.8, noise=0)
print(X)
print(y)
plt.scatter(X[:, 0], X[:, 1]     )
plt.show()
