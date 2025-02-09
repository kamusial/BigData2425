import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
penguins = sns.load_dataset('penguins')

print(penguins.to_string())
sns.pairplot(penguins, hue='species')
plt.show()

penguins_filtered = penguins.drop(columns=['island', 'sex']).dropna()
penguins_features = penguins_filtered.drop(columns=['species'])
penguins_target = pd.get_dummies(penguins_filtered['species'])
# print(penguins_target)
#
from sklearn.model_selection import train_test_split
from tensorflow import keras

X_train, X_test, y_train, y_test = train_test_split(penguins_features, penguins_target, test_size=0.2)

inputs = keras.Input(shape=[X_train.shape[1]])
hidden_layer1 = keras.layers.Dense(4, activation='relu')(inputs)
hidden_layer2 = keras.layers.Dense(4, activation='linear')(hidden_layer1)
hidden_layer3 = keras.layers.Dense(4, activation='linear')(hidden_layer2)
output_layer = keras.layers.Dense(3, activation='softmax')(hidden_layer3)
#
model = keras.Model(inputs=inputs, outputs=output_layer)
print(model.summary())
#
model.compile(optimizer='adam', loss=keras.losses.CategoricalCrossentropy())
result = model.fit(X_train, y_train, epochs=1000)
print(result.history)
sns.lineplot(x=result.epoch, y=result.history['loss'])
plt.show()
#
y_pred = model.predict(X_test)
prediction = pd.DataFrame(y_pred, columns=penguins_target.columns)
print(prediction)
predicted_species = prediction.idxmax(axis='columns')
#
from sklearn.metrics import confusion_matrix
true_species = y_test.idxmax(axis='columns')
matrix = confusion_matrix(true_species, predicted_species)
confusion_df = pd.DataFrame(matrix, index=y_test.columns.values, columns=y_test.columns.values)
confusion_df.index.name = 'True Label'
confusion_df.columns.name = 'Predicted Label'
sns.heatmap(confusion_df, annot=True)
plt.show()
