# from Run import *
from main import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Stats(Team):
    def __init__(self, comp, name, explanvar = None, responvar = None):
        super().__init__(comp, name)
        self.explanvar = explanvar if explanvar else ""
        self.responvar = responvar if responvar else ""

        while "goals" not in self.explanvar:
                self.explanvar = input("Please choose from the following options for your explanatory variable: 1) No. goals scored\n").lower()
                if "goals" not in self.explanvar:
                    print("Invalid Explanatory Variable\nPlease Try Again")

        while "wins" not in self.responvar:
                self.responvar = input("Please choose from the following options for your response variable: 1) No. wins\n").lower()
                if "wins" not in self.responvar:
                    print("Invalid Response Variable\nPlease Try Again")
        print(f"Okay, you have selected your explanatory variable: {self.explanvar} and your response variable: {self.responvar}"
              f"\nWe will now explore using a simpler linear regression model the relationship between"
              f"\n{self.explanvar.upper()} and {self.responvar.upper()}")
        self.get_stats(explanvar, responvar)

    def get_stats(self, explanvar, responvar):
        data = {}
        url = f"https://api.football-data.org/v4/competitions/{self.comp_id}/standings"
        response = (requests.get(url, headers=self.get_headers())).json()

        for standings in response["standings"][0]['table']:
            data[standings['team']['name']] = [standings['goalsFor'], standings['won']]

        df = pd.DataFrame(data, index = ['goals', 'wins'])
        goals = df.loc['goals'].tolist()
        won = df.loc['wins'].tolist()
        sns.scatterplot(x= goals, y= won)
        plt.xlabel('Goals Scored This Season')
        plt.ylabel('Wins This Season')
        plt.title('Goals Scored vs. Wins in the Premier League this Season')
        plt.show()












