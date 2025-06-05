from sklearn.linear_model import LinearRegression

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv
# from Options import Opt
load_dotenv()
api_token = os.getenv("API_TOKEN")

# url = f"https://api.football-data.org/v4/competitions"
# headers = {"X-Auth-Token": f"{api_token}"}
# response = requests.get(url, headers=headers)
# competitions = response.json()['competitions']
# for competition in competitions:
#     print(competition['name'])

# url = f"https://api.football-data.org/v4/competitions"
# headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
# response = requests.get(url, headers=headers)
# print(response.json()['competitions'][1]['name'])


# url = f"https://api.football-data.org/v4/competitions/PL/standings"
# headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
# response = requests.get(url, headers=headers)
#
# table = response.json()['standings'][0]['table']
# for j, i in enumerate(table, start=1):
#     print(f"{j}. {i['team']['name']}")

# url = f"http://api.football-data.org/v4/competitions/PL/teams"
# headers = {"X-Auth-Token": f"{api_token}"}
# response = requests.get(url, headers=headers)
# teams = response.json()['teams']
# for t in teams:
#     print(t['name'])

data = {
    'height': [5, 6, 4, 5, 6, 7],
    'age': [25, 30, 35, 23, 31, 56],
    'city': ['London', 'Paris', 'Berlin', 'London', 'Paris', 'London'],
}

df = pd.DataFrame(data)
print(df)
print(df.loc[0],[1])
# print(f"\n{df.head()}")
# print(f"\n{df.tail()}")
# print(f"\n{df.info()}")
# print(f"\n{df.describe()}")
# print(df['age'].median())
# print(df[df['city'] == 'London'])

# sns.scatterplot(x='age', y='city', data=df)
# plt.title('Age vs City')
# plt.xlabel('Age')
# plt.ylabel('City')
# plt.show()

# X = df[['age']]
# Y = df[['height']]
# model = LinearRegression()
# model.fit(X, Y)
#
# # Predict values
# df['predicted_price'] = model.predict(X)
#
# # Plot
# sns.scatterplot(x='age', y='height', data=df, label='Actual')
# sns.lineplot(x='age', y='predicted_price', data=df, color='red', label='Regression Line')
# plt.title('Simple Linear Regression')
# plt.xlabel('Size (sq ft)')
# plt.ylabel('Price ($k)')
# plt.legend()
# plt.show()
# print(model.score(X, Y))
#
# url = f"https://api.football-data.org/v4/competitions/2021/standings"
# # url = f"https://api.football-data.org/v4/competitions/2021/teams"
# headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
# response = requests.get(url, headers=headers)
# # print(response.json()['standings'][0]['table'][0])
# # print(response.json())
# print(response.json()['standings'][0]['table'][0])
# #
# # for i in response.json()['standings'][0]['table']:
#     print(i['team']['name'])
#     print(i['goalsFor'])
#     print(i['won'])



