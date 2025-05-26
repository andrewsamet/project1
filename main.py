import requests
import os
from dotenv import load_dotenv
# from Options import Opt
load_dotenv()
api_token = os.getenv("API_TOKEN")

class Team():
    def __init__(self, name):
        self.name = name
        url = f"https://api.football-data.org/v4/competitions/PL/teams"
        headers = {"X-Auth-Token": f"{api_token}"}
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







