from main import *
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class Options_Comp(Competition):
    def __init__(self, comp, responvar = None, explanvar = None):
        """
        This is the constructor method for the Options_Comp class. This is for the competition options.
        Args:
            comp: this requires a valid competition, which it inherits from Competition.
            responvar: a response variable to use in our simple linear regression model
            explanvar: a explanatory variable to use in our simple linear regression model
        """
        super().__init__(comp)
        self.explanvar = explanvar
        self.responvar = responvar

    def get_variables(self):
        """
        This method gets the variables for our simple linear regression model.
        Returns: the variables selected by the user.

        """
        while True:
            explanvar = input("Please Select From The Following Options For Your Explanatory Variable: 1) goalsFor 2) goalsAgainst 3) goalDifference\n")
            if explanvar in ["goalsFor", "goalsAgainst", "goalDifference"]:
                self.explanvar = explanvar
                break
            else:
                print("Invalid Explanatory Variable\nPlease Try Again")
        while True:
            responvar = input("Please choose from the following options for your response variable: 1) Won 2) Draw 3) Lost 4) Points\n")
            if responvar.lower() in ["won", "draw", "lost", "points"]:
                self.responvar = responvar.lower()
                break
            else:
                print("Invalid Response Variable\nPlease Try Again")

        print(f"Okay, you have selected your explanatory variable: {self.explanvar} and your response variable: {self.responvar}"
                f"\nWe will now explore using a simpler linear regression to model the relationship between"
                f"\n{self.explanvar.upper()} and {self.responvar.upper()}")


    def get_stats(self):
        """
        This method gets the relevant stats for our simple linear regression model.
        Returns: the relevant stats for our simple linear regression model.

        """
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
        """
        This method calculates the r-squared value for the simple linear regression model.
        Args:
            r_squared: this method must be given an r squared value.

        Returns: the r-squared value for the simple linear regression model.

        """
        ask = input(f"\nWould you like a statistic to analyse how closely {self.explanvar} and {self.responvar} reflect a simple linear regression?\n")
        if ask == "yes":
            print(f"R-squared: {r_squared:.2f}")

            interpret = input("Would you like an interpretation of this 'r-value'?\n")
            if interpret == "yes":
                if r_squared >= 0.9:
                    print(f"An 'r-value' of {r_squared:.2f} means very strong correlation between {self.explanvar} and {self.responvar}\n")
                elif 0.7 <= r_squared < 0.9:
                    print(f"An 'r-value' of {r_squared:.2f} means strong correlation between {self.explanvar} and {self.responvar}\n")
                elif 0.5 <= r_squared < 0.7:
                    print(f"An 'r-value' of {r_squared:.2f} means moderate correlation between {self.explanvar} and {self.responvar}\n")
                elif 0.3 <= r_squared < 0.5:
                    print(f"An 'r-value' of {r_squared:.2f} means weak correlation between {self.explanvar} and {self.responvar}\n")
                else:
                    print(f"An 'r-value' of {r_squared:.2f} means there is no correlation between {self.explanvar} and {self.responvar}\n")

    def get_table(self):
        """
        This method displays the league table for the competition the user selected.
        Returns: the league table for the relevant competition.

        """
        url = f"https://api.football-data.org/v4/competitions/{self.comp_id}/standings"
        response = requests.get(url, headers=self.get_headers())

        table = response.json()['standings'][0]['table']
        for j, i in enumerate(table, start=1):
            print(f"{j}. {i['team']['name']}")





