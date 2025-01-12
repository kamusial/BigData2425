import pandas as pd
import json

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return pd.DataFrame(data)
        except FileNotFoundError:
            print(f'Nie znaleziono pliku')
            return pd.DataFrame()


class UserAnalyzer:
    def __init__(self, user_data):
        self.user_data = user_data

    def average_age(self):
        return self.user_data['age'].mean()

    def most_popular_hobby(self):
        return self.user_data['hobby'].mode()[0]

    def country_distribution(self):
        return self.user_data['country'].value_counts()

data_loader = DataLoader('data\\users.json')
user_data = data_loader.load_data()

analyzer = UserAnalyzer(user_data)
avg_age = analyzer.average_age()
print(f'Average Age: {round(avg_age, 2)}')

popular_hobby = analyzer.most_popular_hobby()
print(f"Most Popular Hobby: {popular_hobby}")

country_dist = analyzer.country_distribution()
print(country_dist)
