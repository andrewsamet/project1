import requests
# """requests allows us to access data online. headers means any extra information thats needed for the url,
# e.g. our AIP key"""
# url = f"https://api.football-data.org/v4/teams/66/matches"
# headers = {"X-Auth-Token": "2e37a6b44f0c47f18526dec884897e45"}
# response = requests.get(url, headers = headers)
# """We iterate through the lists of matches, and select home team of each match and the name, like
# a dictionary"""
# matches = response.json()['matches']
# for i in matches:
#     hometeam = i['homeTeam']['name']
#     awayteam = i['awayTeam']['name']
#     print(f"{hometeam} vs {awayteam}")
premier_league_teams = {
    "Arsenal": 57,
    "Aston Villa": 58,
    "Bournemouth": 1044,
    "Brentford": 402,
    "Brighton": 397,
    "Burnley": 328,
    "Chelsea": 61,
    "Crystal Palace": 354,
    "Everton": 62,
    "Fulham": 63,
    "Liverpool": 64,
    "Luton Town": 389,
    "Manchester City": 65,
    "Manchester United": 66,
    "Newcastle United": 67,
    "Nottingham Forest": 351,
    "Sheffield United": 356,
    "Tottenham Hotspur": 73,
    "West Ham United": 563,
    "Wolverhampton Wanderers": 76
}

class Team():
    premier_league_teams = {
        "Arsenal": 57,
        "Aston Villa": 58,
        "Bournemouth": 1044,
        "Brentford": 402,
        "Brighton": 397,
        "Burnley": 328,
        "Chelsea": 61,
        "Crystal Palace": 354,
        "Everton": 62,
        "Fulham": 63,
        "Liverpool": 64,
        "Luton Town": 389,
        "Manchester City": 65,
        "Manchester United": 66,
        "Newcastle United": 67,
        "Nottingham Forest": 351,
        "Sheffield United": 356,
        "Tottenham Hotspur": 73,
        "West Ham United": 563,
        "Wolverhampton Wanderers": 76
    }

    def __init__(self, name):
        if name in Team.premier_league_teams:
            self.name = name
            self.team_id = self.premier_league_teams[name]
            self.fixtures = []
            url = f"https://api.football-data.org/v4/teams/{self.team_id}/matches"
            headers = {"X-Auth-Token" : "2e37a6b44f0c47f18526dec884897e45"}
            response = requests.get(url, headers = headers)

            for i in response.json()['matches']:
                hometeam = i['homeTeam']['name']
                awayteam = i['awayTeam']['name']
                self.fixtures.append(f"{hometeam} vs {awayteam}")
        else:
            raise ValueError(f"{name} is not a valid premier league team, sorry.")

    def show_fixtures(self):
        for i in self.fixtures:
            print(i)
        return

# ManUtd = Team(66, 'Man Utd')
# ManUtd.show_fixtures()
Chosen_team = input("What team would you like to explore?")
team = Team(Chosen_team)
team.show_fixtures()



