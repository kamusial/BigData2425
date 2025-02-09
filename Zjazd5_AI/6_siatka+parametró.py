import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('dane\\heart.csv', comment='#')
print(df.head().to_string())

X = df.iloc[:, :-1]
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier(criterion='gini', max_depth=None, min_samples_split=5)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))
print(pd.DataFrame(model.feature_importances_, X.columns))

print('Siatka parametrów')
model = DecisionTreeClassifier()
params = {
    'max_depth': [2, 3, 4],
    'criterion': ['gini', 'entropy', 'log_loss']
}

grid = GridSearchCV(model, params, cv=5, verbose=2)
grid.fit(X_train, y_train)
print(f'parametry: {grid.best_params_}')
print(f'Wynik: {grid.best_score_}')



