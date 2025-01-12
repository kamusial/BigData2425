import matplotlib.pyplot as plt

# y = 5x - 2
X = [i+1 for i in range(0,10)]
Y = [5*i - 2 for i in X]

print(X)
print(Y)

plt.plot(X, Y, 'ro--')
plt.show()