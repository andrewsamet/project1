from main import Team, Competition
from Options import Options_Team
from Stats import Options_Comp
import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_token = os.getenv("API_TOKEN")

class Run:
    def get_headers(self):
        """
        Returns: Method to get headers, more specifically to get my unique API token.
        """
        return {"X-Auth-Token": f"{api_token}"}

    def __init__(self):
        """
        User selects a competition or can choose to see all valid competitions.
        Then the user chooses whether to explore his competition or to explore a specific team.
        If the user selects "team", ie to explore a specific team. Then he selects a specific team and
        then self.what_to_do is called.
        """
        available_comps = ['Premier League', 'Serie A', 'Bundesliga', 'Primera Division', 'Ligue 1']
        while True:
            comp = input("Please Select A Competition: (To See A List Of Valid Competitions Please Enter '?')\n")
            if comp == "?":
                print("Available Competitions: "+", ".join(available_comps)+"\n")
            else:
                try:
                    self.competition = Competition(comp)
                    break
                except ValueError as e:
                    print(e)
                    print("Please Try Again")
                except requests.exceptions.HTTPError as errh:
                    print("HTTP Error:", errh)
                except requests.exceptions.ConnectionError as errc:
                    print("Error Connecting to API:", errc)
                except requests.exceptions.Timeout as errt:
                    print("Request Timed Out:", errt)
                except requests.exceptions.RequestException as err:
                    print("Something went wrong with the request:", err)

        while True:
            choice = input("Please Select From The Following Options:\nA) Competition B) Team C) Main Menu D) Exit\n")
            if choice.lower().strip() == "competition":
                while True:
                    self.stats = Options_Comp(self.competition.competition)
                    opt = input("\nPlease Select From The Following Options: A) Stats B) Table C) Main Menu D) Exit\n")
                    if "stats" in opt.lower().strip():
                        self.stats.get_variables()
                        self.stats.get_stats()
                    elif "table" in opt.lower().strip():
                        self.stats.get_table()
                    elif "main menu" in opt.lower().strip():
                        self.__init__()
                        return
                    elif "exit" in opt.lower().strip():
                        self.competition.exit()
                    else:
                        print("Invalid Option\nPlease Try Again\n")

            elif choice.lower().strip() == "team":
                    while True:
                        team = input(f"Please Select A Team In The {self.competition.competition.upper()} (To See A List Of Valid Teams In The {self.competition.competition.upper()} PLease Enter '?')?\n")
                        if team == "?":
                            teams = []
                            url = f"https://api.football-data.org/v4/competitions/{self.competition.comp_id}/teams"
                            response = requests.get(url, headers=self.get_headers())
                            for i in response.json()['teams']:
                                teams.append(i['name'])
                            print("Available Teams: "+", ".join(teams)+"\n")
                        else:
                            try:
                                self.team = Team(self.competition.competition, team)
                                self.options = Options_Team(self.competition.competition, team)
                                self.what_to_do()
                                return
                            except ValueError as e:
                                print(e)
                                print("Please Try Again\n")
                            except requests.exceptions.HTTPError as errh:
                                print("HTTP Error:", errh)
                            except requests.exceptions.ConnectionError as errc:
                                print("Error Connecting to API:", errc)
                            except requests.exceptions.Timeout as errt:
                                print("Request Timed Out:", errt)
                            except requests.exceptions.RequestException as err:
                                print("Something went wrong with the request:", err)
            elif choice.lower().strip() == "main menu":
                self.__init__()
            elif choice.lower().strip() == "exit":
                self.competition.exit()
            else:
                print("Invalid Option\nPlease Try Again\n")

    def what_to_do(self):
        while True:
                to_do = input(f"Please Select From The Following Options: A) Fixtures B) Squad C) Position D) Main Menu E) Exit\n").lower()
                if "fixture" in to_do or "fixtures" in to_do:
                    self.options.show_fixtures()
                elif "position" in to_do:
                    self.options.position()
                elif "exit" in to_do:
                    self.competition.exit()
                elif "squad" in to_do:
                    self.options.squad()
                elif "main menu" in to_do:
                    self.__init__()
                    return
                else:
                    print("Invalid Request\nPlease Try Again")
                    return self.what_to_do()



Run()