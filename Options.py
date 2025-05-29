import requests
from main import Team

class Opt(Team):
    def __init__(self, comp, name):
        super().__init__(comp, name)

    def show_fixtures(self):
        url = f"https://api.football-data.org/v4/teams/{self.team_id}/matches"
        response = requests.get(url, headers=self.get_headers())
        for i in response.json()['matches']:
            hometeam = i['homeTeam']['name']
            awayteam = i['awayTeam']['name']
            self.fixtures.append(f"{hometeam} vs {awayteam}")
        for i in self.fixtures:
            print(i)

    def see_table(self):
        url = f"https://api.football-data.org/v4/competitions/{self.comp_id}/standings"
        response = requests.get(url, headers=self.get_headers())

        table = response.json()['standings'][0]['table']
        for j, i in enumerate(table, start=1):
            print(f"{j}. {i['team']['name']}")

    def position(self):
        url = f"https://api.football-data.org/v4/competitions/{self.comp_id}/standings"
        response = requests.get(url, headers=self.get_headers())

        table = response.json()['standings'][0]['table']

        for entry in table:
            if entry['team']['name'].lower().removesuffix("fc").strip() == self.name:
                print(f"{entry['team']['name']} currently sit at position {entry['position']} in the table.")
                break