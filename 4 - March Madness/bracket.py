#from .team import Team
import pandas as pd
import random


class Team:

    defeated_teams = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# read raw csv file for teams and only pull the first two columns (id, team_name)
bracket_df = pd.read_csv('bracket-00.csv')
bracket_df = bracket_df[['team_id', 'team_name']]
# Grab only the first 64 rows - we need number of teams to be a power of 2.
bracket_df = bracket_df.loc[:63]
bracket_df.to_csv('teams.csv', header=False, index=False)
#print(len(bracket_df))
teams = []
bracket = []


def create_teams(file):
# Read from the teams.csv file and populate the teams list with Team objects.
    with open(file) as f:
        for line in f:
            split_line = line.split(',')
            teams.append(Team(split_line[0], split_line[1]))

create_teams('teams.csv')
#print(teams)

def generate_bracket(teams):
    # Generate bracket from the teams list the bracket list will be a list
    # of randomly generated tuples between the teans objects such as 
    # bracket = [(Weber State. Gonzaga), (Baylor, Nebraska)]

    # Number of 'games' to be played as if there are 64 teams, there's going to
    # be teams/2 games. In this case 32 games.
    iterations = len(teams) // 2

    for i in range(iterations):
        team_1 = random.choice(teams)
        teams.remove(team_1)
        team_2 = random.choice(teams)
        teams.remove(team_2)

        bracket.append((team_1, team_2))

generate_bracket(teams)
#print(bracket)
#print(len(bracket))

def play_tournament(bracket):
    # Function to play out the tournament by providing an initial bracket list
    
    for match in bracket:
        # generates True/False based on random. If True, first time in the 
        # tuple wins, else the second team wins.
        selection = random.random() > 0.5

        if not selection:
            winner = match[0]
            loser = match[1]
        else:
            winner = match[1]
            loser = match[0]
        
        winner.defeated_teams.append(loser)
        winners.append(winner)

winners = []
play_tournament(bracket)
print(winners)
print(len(winners))