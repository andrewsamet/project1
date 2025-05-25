from main import Team
from Options import Opt

class Run():
    def __init__(self):
        name = input("What team would you like to explore? \n")
        try:
            self.options = Opt(name)
            self.what_to_do()
        except ValueError as e:
            print(e)
            print("\nPlease Try Again\n")
            self.__init__()

    def what_to_do(self):
        first_time = True
        while True:
            if first_time:
                to_do = input(f"What woud you like to explore about {self.options.name}? \n").lower()
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
                print("Exiting Program")
                break
            else:
                print("Invalid Request\nPlease Try Again")
                return self.what_to_do()

    # def exit(self):
    #     return



Run()