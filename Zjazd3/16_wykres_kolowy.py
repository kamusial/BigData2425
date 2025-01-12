import matplotlib.pyplot as plt
expenses = ["mieszkanie","media","jedzenie","rozrywka","nauka","inwestycje"]
values = [3000, 300, 1000, 500, 200, 1500]
# explode = [0, 0, 0.2, 0, 0.4, 0]
explode = [0 for i in expenses]
explode[3] = 0.3
explode[expenses.index('inwestycje')] = 0.2

plt.pie(values, labels=expenses, explode=explode,
        autopct="%.2f",
        shadow=True)
plt.show()