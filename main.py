import requests
import os
from dotenv import load_dotenv
# from Options import Opt
load_dotenv()
api_token = os.getenv("API_TOKEN")

class Competition:
    def get_headers(self):
        return {"X-Auth-Token": f"{api_token}"}

    def __init__(self, comp):
        self.competition = comp
        url = f"https://api.football-data.org/v4/competitions"
        response = requests.get(url, headers=self.get_headers())
        competitions = response.json()['competitions']
        found = False
        for competition in competitions:
            normal_competition = competition['name'].lower().strip()
            if normal_competition == self.competition.lower().strip():
                self.comp_id = competition['id']
                found = True
                break
        if not found:
            raise ValueError(f"{self.competition} is not a valid competition, sorry.")

class Team(Competition):
    def __init__(self, comp, name):
        super().__init__(comp)
        self.name = name
        url = f"https://api.football-data.org/v4/competitions/{self.comp_id}/teams"
        response = requests.get(url, headers=self.get_headers())
        teams = response.json()['teams']
        found = False
        for team in teams:
            normal_name = team['name'].lower().removesuffix("fc").strip()
            if normal_name == self.name.lower().strip():
                self.team_id = team['id']
                found = True
                break
        if not found:
            raise ValueError(f"{name} is not a valid premier league team, sorry.")

        self.fixtures = []







