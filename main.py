import requests
import sys
import os
from dotenv import load_dotenv
load_dotenv()
api_token = os.getenv("API_TOKEN")

class Competition():
    def get_headers(self):
        """

        Returns:  Method to get headers, more specifically to get my unique API token.

        """
        return {"X-Auth-Token": f"{api_token}"}

    def __init__(self, comp):
        """
        This constructor creates a Competition object.
        Args:
            comp: you must pass this constructor a competition name. The constructor then
        checks to see if your competition name is a valid one.
        """
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

    def exit(self):
        """
        This method exits the code
        Returns: exits the code

        """
        sys.exit("Exiting...")

class Team(Competition):
    def __init__(self, comp, name):
        """
        This constructor creates a Team object. This class inherits from Competition, as for a team to be chosen we must
        have this team's competition too.
        Args:
            comp: competition name
            name: you must pass this constructor a team name. The constructor then
        checks to see if your team name is a valid one.
        """
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
            raise ValueError(f"{name} is not a valid {self.competition.strip()} team, sorry.")







