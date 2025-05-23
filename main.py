import requests

class Team():
    def __init__(self, name):
        self.name = name
        url = f"https://api.football-data.org/v4/competitions/PL/teams"
        headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
        response = requests.get(url, headers=headers)
        teams = response.json()['teams']
        for team in teams:
            if team['name'] == name:
                self.team_id = team['id']
                break
            else:
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
                break

    def what_to_do(self, team):
        to_do = input(f"What woud you like to explore about {team.name}? \n")
        if to_do == "Fixture List":
            return team.show_fixtures()
        elif to_do == "See Table":
            return team.see_table()
        else:
            print("Invalid Request\nPlease Try Again")
            return self.what_to_do(team)

app = Run()
app.what_team()




