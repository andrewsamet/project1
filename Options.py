import requests
from main import Team

class Opt(Team):
    def show_fixtures(self):
        url = f"https://api.football-data.org/v4/teams/{self.team_id}/matches"
        headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
        response = requests.get(url, headers=headers)
        for i in response.json()['matches']:
            hometeam = i['homeTeam']['name']
            awayteam = i['awayTeam']['name']
            self.fixtures.append(f"{hometeam} vs {awayteam}")
        for i in self.fixtures:
            print(i)

    def see_table(self):
        url = f"https://api.football-data.org/v4/competitions/PL/standings"
        headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
        response = requests.get(url, headers=headers)

        table = response.json()['standings'][0]['table']
        for j, i in enumerate(table, start=1):
            print(f"{j}. {i['team']['name']}")

    def position(self):
        url = f"https://api.football-data.org/v4/competitions/PL/standings"
        headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
        response = requests.get(url, headers=headers)

        table = response.json()['standings'][0]['table']

        for entry in table:
            if entry['team']['name'].lower().removesuffix("fc").strip() == self.name:
                print(f"{entry['team']['name']} currently sit at postion {entry['position']} in the table.")
                break