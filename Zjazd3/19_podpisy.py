import matplotlib.pyplot as plt
import math

Epsilon = [i for i in range(1,10)]
Sigma = [math.log10(i) for i in Epsilon]
plt.plot(Epsilon, Sigma)
plt.title(r'Wykres naprezenia $\sigma (\delta \epsilon)$')
plt.xlabel(r'$\frac{\delta \epsilon}{\epsilon}$')
plt.ylabel(r'$\sigma$', size=15)
plt.text(5, 0.8, r'$\sigma = f(\delta \ epsilon)$')
plt.show()

# Dokumentacja matplotlib: Matplotlib: Python plotting — Matplotlib 3.4.2 documentation
# Tutorial prostych wykresów: Pyplot tutorial — Matplotlib 3.4.2 documentation
# Przykładowe wykresy: Sample plots in Matplotlib — Matplotlib 3.4.2 documentation