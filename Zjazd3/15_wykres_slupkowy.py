import matplotlib.pyplot as plt
import random

names = ['Ania', 'Kasia', 'Pawel', 'Mariusz', 'Roman']
ages = [random.randint(18, 70) for name in names]

plt.bar(names, ages, color=['red', 'green', 'blue'])
plt.xticks(names)
plt.yticks(ages)
plt.show()
