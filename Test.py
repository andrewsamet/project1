import requests
# url = f"https://api.football-data.org/v4/competitions/PL/teams"
# headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
# response = requests.get(url, headers=headers)
#
# teams = response.json()['teams']
# for i in teams:
#     if i['name'] == "Arsenal FC":
#         print(i['name'])

url = f"https://api.football-data.org/v4/competitions/PL/standings"
headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
response = requests.get(url, headers=headers)

# table = response.json()['standings'][0]['table']
# for j,i in enumerate(table, start=1):
#     print(f"{j}. {i['team']['name']}")

position = response.json()['standings'][0]['table'][1]['team']['name'].lower().removesuffix("fc").strip()
print(position)