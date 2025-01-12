import random
import matplotlib.pyplot as plt

data1 = [random.randint(0, 20) for i in range(1000)]
data2 = [random.gauss(mu=10, sigma=5) for i in range(1000)]
bins = 21
plt.subplot(2, 1, 1); plt.hist(data1, bins)
plt.subplot(2, 1, 2); plt.hist(data2, bins, facecolor='red', edgecolor='black')
plt.show()

# Ćwiczenie: Wygeneruj 1000 liczb z rozkładu Gamma dla określonego k i theta (w dokumentacji random pod
# nazwami alpha i beta) i narysuj histogram. Sprawdź zgodność kształtu histogramu np. z danymi z wikipedii:
# https://en.wikipedia.org/wiki/Gamma_distribution
