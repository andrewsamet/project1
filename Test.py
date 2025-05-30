import requests
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

url = f"https://api.football-data.org/v4/competitions"
headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
response = requests.get(url, headers=headers)
print(response.json()['competitions'][1]['name'])


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
