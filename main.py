import requests
# from Options import Opt

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







