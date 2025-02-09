import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import shutil
import sys
import tensorflow as tf
from collections import Counter
from numpy.random import seed
from sklearn.datasets import load_breast_cancer, load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score as acc_score
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold, train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import *
from tensorflow.keras.datasets import mnist, cifar10
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 10000)
pd.set_option('display.max_colwidth', 10000)
np.set_printoptions(linewidth=2000)

X, y = load_breast_cancer(return_X_y=True, as_frame=True)
print(X.head())
print(X.shape)
print(X.describe())
print(Counter(y))

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model = MLPClassifier(max_iter=1000, hidden_layer_sizes=(10, 10, 10))
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(accuracy_score(y_test, y_pred))

score = []
kfold = RepeatedStratifiedKFold(n_splits=10, n_repeats=5)
for train, test in kfold.split(X, y):
    model = MLPClassifier(max_iter=5000, hidden_layer_sizes=(100, 100, 100, 100, 100))
    X_train, X_test = X.iloc[train, :], X.iloc[test,:]
    y_train, y_test = y.iloc[train], y.iloc[test]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score.append(accuracy_score(y_test, y_pred))
print(score)
plt.plot(score)
plt.show()