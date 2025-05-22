import requests
"""requests allows us to access data online. headers means any extra information thats needed for the url, 
e.g. our AIP key"""
url = f"https://api.football-data.org/v4/teams/66/matches"
headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
response = requests.get(url, headers = headers)
"""We iterate through the lists of matches, and select home team of each match and the name, like
a dictionary"""
matches = response.json()['matches']
for i in matches:
    hometeam = i['homeTeam']['name']
    awayteam = i['awayTeam']['name']
    print(f"{hometeam} vs {awayteam}")
