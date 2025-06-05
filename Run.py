from main import Team, Competition
from Options import Opt
from Stats import Stats
import sys

class Run:
    def __init__(self, comp=None):
        if comp is None:
            comp = input("What competition would you like to explore? \n")
            try:
                self.competition = Competition(comp)
            except ValueError as e:
                print(e)
                print("\nPlease Try Again\n")
                self.__init__()
        name = input(f"What team would you like to explore in the {comp.strip().lower()}? \n")
        try:
            self.team = Team(comp, name)
        except ValueError as e:
            print(e)
            print("\nPlease Try Again\n")
            self.__init__(comp)

        self.options = Opt(comp, name)
        self.what_to_do()

    def what_to_do(self):
        first_time = True
        while True:
            if first_time:
                to_do = input(f"What would you like to explore about {self.options.name}? \n").lower()
                first_time = False
            else:
                to_do = input(f"\nWhat else would you like to explore about {self.options.name}? \n").lower()

            if "fixture" in to_do or "fixtures" in to_do:
                self.options.show_fixtures()
            elif "table" in to_do:
                self.options.see_table()
            elif "position" in to_do:
                self.options.position()
            elif "exit" in to_do:
                sys.exit("Exiting Programme...")
            elif "stats" in to_do:
                self.stats = Stats(self.team.competition, self.team.name)
            elif "squad" in to_do:
                self.options.squad()
            else:
                print("Invalid Request\nPlease Try Again")
                return self.what_to_do()

    # def exit(self):
    #     return



Run()