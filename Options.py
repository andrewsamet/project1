import requests
from main import Team

class Options_Team(Team):
    def __init__(self, comp, name):
        """
        This constructor method is for the options for the team selection.
        Args:
            comp: valid competition required, which it inherits from Team
            name: valid team name, which it inherits from Team.
        """
        super().__init__(comp, name)
        self.fixtures = []

    def show_fixtures(self):
        """
        This method is to show all the fixtures available for the team.
        Returns: the fixtures available for the team.

        """
        url = f"https://api.football-data.org/v4/teams/{self.team_id}/matches"
        response = requests.get(url, headers=self.get_headers())
        for i in response.json()['matches']:
            hometeam = i['homeTeam']['name']
            awayteam = i['awayTeam']['name']
            self.fixtures.append(f"{hometeam} vs {awayteam}")
        for i in self.fixtures:
            print(i)

    def position(self):
        """
        This method is to get the current position of the team in the table.
        Returns: current position of the team in the table.

        """
        url = f"https://api.football-data.org/v4/competitions/{self.comp_id}/standings"
        response = requests.get(url, headers=self.get_headers())

        table = response.json()['standings'][0]['table']

        for entry in table:
            if entry['team']['name'].lower().removesuffix("fc").strip() == self.name:
                print(f"{entry['team']['name']} currently sit at position {entry['position']} in the table.")
                break

    def squad(self):
        """
        This method is to get the entire current squad of the team selected.
        Returns: the full squad of the team selected.

        """
        url = f"https://api.football-data.org/v4/teams/{self.team_id}"
        response = requests.get(url, headers=self.get_headers())

        try:
            squad = response.json()['squad']
            players = []
            for i in squad:
                players.append(i['name'])
            print(f"{self.name.upper()} Squad: {', '.join(players)}")
        except KeyError as e:
            print(e)
            print("Information Not Available")


