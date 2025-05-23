import requests

class Team():
    def __init__(self, name):
        self.name = name
        url = f"https://api.football-data.org/v4/competitions/PL/teams"
        headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
        response = requests.get(url, headers=headers)
        teams = response.json()['teams']
        found = False
        for team in teams:
            normal_name = team['name'].lower().removesuffix("fc").strip()
            if normal_name == name:
                self.team_id = team['id']
                found = True
                break
        if found == False:
            raise ValueError(f"{name} is not a valid premier league team, sorry.")

        self.fixtures = []
        url = f"https://api.football-data.org/v4/teams/{self.team_id}/matches"
        headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
        response = requests.get(url, headers=headers)
        for i in response.json()['matches']:
            hometeam = i['homeTeam']['name']
            awayteam = i['awayTeam']['name']
            self.fixtures.append(f"{hometeam} vs {awayteam}")

    def show_fixtures(self):
        for i in self.fixtures:
            print(i)
        return

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
                print(f"{entry['position']}. {entry['team']['name']}")
                break

class Run():
    def what_team(self):
        name = input("What team would you like to explore? \n")
        while True:
            try:
                team = Team(name)
                self.what_to_do(team)
                break
            except ValueError as e:
                print(e)
                print("\nPlease Try Again\n")
                self.what_team()
                break

    def what_to_do(self, team):
        to_do = input(f"What woud you like to explore about {team.name}? \n").lower()
        if "fixture" in to_do or "fixtures" in to_do:
            return team.show_fixtures()
        elif "table" in to_do:
            return team.see_table()
        elif "position" in to_do:
            return team.position()
        else:
            print("Invalid Request\nPlease Try Again")
            return self.what_to_do(team)

app = Run()
app.what_team()




