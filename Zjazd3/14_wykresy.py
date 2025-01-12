import matplotlib.pyplot as plt

# y = 5x - 2
X = [i+1 for i in range(0,10)]
Y = [5*i - 2 for i in X]

print(X)
print(Y)

plt.plot(X, Y, 'ro--')
plt.show()

# funkcja 1: y = 5x - 2 ; funkcja 2: y = -2x + 5 ; funkcja 3: y = 3x + 3

X = [i+1 for i in range(-10, 10)]
Y1 = [ 5*i - 2 for i in X]
Y2 = [-2*i + 5 for i in X]
Y3 = [ 3*i + 3 for i in X]
plt.axhline()
plt.axvline()
plt.plot(X, Y1, 'ro-')
plt.plot(X, Y2, 'b^-')
plt.plot(X, Y3, 'gs--')
plt.xlabel('punkty x')
plt.ylabel('wartości x')
plt.title('Wykresy')
plt.show()

plt.plot(X, Y1, 'ro-', X, Y2, 'b^-', X, Y3, 'gs--')
plt.show()

