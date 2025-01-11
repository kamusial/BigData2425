import requests
import pandas as pd
from pprint import pprint

# 1. POBIERANIE DANYCH
url_users = "https://jsonplaceholder.typicode.com/users"
url_posts = "https://jsonplaceholder.typicode.com/posts"
url_comments = "https://jsonplaceholder.typicode.com/comments"

response_users = requests.get(url_users)
response_posts = requests.get(url_posts)
response_comments = requests.get(url_comments)

if response_users.status_code == response_posts.status_code == response_comments.status_code == 200:
    data_users = response_users.json()
    data_posts = response_posts.json()
    data_comments = response_comments.json()
else:
    raise Exception('Nie udało się pobrać danych')

pprint(data_users)