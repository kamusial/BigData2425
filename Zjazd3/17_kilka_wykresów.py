import matplotlib.pyplot as plt
import random
import math

X = [x for x in range(0, 4*360+1, 10)]
Y1 = [math.cos(math.radians(i)) for i in X]
Y2 = [random.random() for i in X]
plt.subplot(1, 3, 1)  # piony, poziomy, index
plt.plot(X,Y1,"r.-")
plt.subplot(1, 3, 3)
plt.plot(X,Y2,"bs:")
plt.show()

# Ćwiczenie - stwórz wykres składający się z 4 podwykresów (2x2):
# 1. sinus kąta od 0 do 360 (zielona linia przerywana z gwiazdkami)
# 2. 100 losowych liczb od 0 do 1 (niebieskie punkty)
# 3. wykres funkcji x**2 - x - 2 (czerwona linia z diamentami, w zakresie -5:5)
# 4. wykres kołowy - czas spędzony na aktywnościach w ciągu dnia (np. spanie, praca, rozrywka, nauka)
