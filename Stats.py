# from Run import *
from main import *
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.linear_model import LinearRegression


class Options_Comp(Competition):
    def __init__(self, comp, responvar = None, explanvar = None):
        super().__init__(comp)
        self.explanvar = explanvar
        self.responvar = responvar

    def get_variables(self):
            while True:
                explanvar = input("Please Select From The Following Options For Your Explanatory Variable: 1) goalsFor 2) goalsAgainst 3) goalDifference\n")
                if explanvar in ["goalsFor", "goalsAgainst", "goalDifference"]:
                    self.explanvar = explanvar
                    break
                else:
                    print("Invalid Explanatory Variable\nPlease Try Again")
            while True:
                responvar = input("Please choose from the following options for your response variable: 1) Won 2) Draw 3) Lost 4) Points\n")
                if responvar in ["won", "draw", "lost", "points"]:
                    self.responvar = responvar
                    break
                else:
                    print("Invalid Response Variable\nPlease Try Again")

            print(f"Okay, you have selected your explanatory variable: {self.explanvar} and your response variable: {self.responvar}"
                  f"\nWe will now explore using a simpler linear regression to model the relationship between"
                  f"\n{self.explanvar.upper()} and {self.responvar.upper()}")


    def get_stats(self):
        data = {}
        url = f"https://api.football-data.org/v4/competitions/{self.comp_id}/standings"
        response = (requests.get(url, headers=self.get_headers())).json()

        for standings in response["standings"][0]['table']:
            data[standings['team']['name']] = [standings[self.explanvar], standings[self.responvar]]

        df = pd.DataFrame(data).T
        df.columns = [self.explanvar,self.responvar]
        X = df[[f'{self.explanvar}']]
        y = df[f'{self.responvar}']
        model = LinearRegression()
        model.fit(X, y)
        df['y_pred'] = model.predict(X)
        r_squared = model.score(X, y)
        plt.scatter(X, y)
        plt.plot(X, df['y_pred'], color = 'red')
        plt.xlabel(f'{self.explanvar}')
        plt.ylabel(f'{self.responvar}')
        plt.title(f'{self.explanvar} vs. {self.responvar}')
        plt.show()

        self.r_squared(r_squared)

    def r_squared(self, r_squared):
        ask = input(f"\nWould you like a statistic to analyse how closely {self.explanvar} and {self.responvar} reflect a simple linear regression?\n")
        if ask == "yes":
            print(f"R-squared: {r_squared:.2f}")

            interpret = input("Would you like an interpretation of this 'r-value'?\n")
            if interpret == "yes":
                if r_squared > 0.8:
                    print(f"An 'r-value' of {r_squared:.2f} means strong correlation between {self.explanvar} and {self.responvar}")
                else:
                    print(f"An 'r-value' of {r_squared:.2f} means weak correlation between {self.explanvar} and {self.responvar}")

    def get_table(self):
        url = f"https://api.football-data.org/v4/competitions/{self.comp_id}/standings"
        response = requests.get(url, headers=self.get_headers())

        table = response.json()['standings'][0]['table']
        for j, i in enumerate(table, start=1):
            print(f"{j}. {i['team']['name']}")





