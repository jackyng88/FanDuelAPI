import pandas as pd
import random
import math


class Team:
    # Class for Team object
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.defeated_teams = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# Following lines are optional as the files have been provided.
# read raw csv file for teams and only pull the first two columns (id, team_name)
bracket_df = pd.read_csv('bracket-00.csv')
bracket_df = bracket_df[['team_id', 'team_name']]
# Grab only the first 64 rows - we need number of teams to be a power of 2.
bracket_df = bracket_df.loc[:63]
bracket_df.to_csv('teams.csv', header=False, index=False)


def create_teams(file):
# Read from the teams.csv file and populate the teams list with Team objects.
    with open(file) as f:
        for line in f:
            split_line = line.split(',')
            teams.append(Team(split_line[0], split_line[1]))
    return teams

def generate_bracket(teams):
    # Generate bracket from the teams list the bracket list will be a list
    # of randomly generated tuples between the teans objects such as 
    # bracket = [(Weber State. Gonzaga), (Baylor, Nebraska)]

    # Number of 'games' to be played as if there are 64 teams, there's going to
    # be teams/2 games. In this example 32 games.
    iterations = len(teams) // 2
    bracket = []

    for i in range(iterations):
        team_1 = random.choice(teams)
        teams.remove(team_1)
        team_2 = random.choice(teams)
        teams.remove(team_2)

        bracket.append((team_1, team_2))
    return bracket

def play_tournament(bracket, teams):
    # Function to play out the tournament by providing an initial bracket list
    
    # num_rounds will equal the log base 2 of the current number of teams i.e.
    # the number of "levels" in a binary tree.
    num_rounds = int(math.log(len(teams), 2))
    #print(num_rounds)

    for i in range(num_rounds):
        if len(winners) > 0:
            # If winners list is currently populated i.e. past the first round
            bracket = generate_bracket(winners)
        else:
            # Generate the bracket if no games have been played yet.
            bracket = generate_bracket(teams)

        for match in bracket:
            # Iterate through the match in the brackets list. Match is in the 
            # form of a tuple of Team objects i.e. (Gonzaga, Witchita State)

            # generates True/False based on random. If True, first team in the 
            # tuple wins, else the second team wins.
            selection = random.random() >= 0.5
            # Keep track of the winner and loser
            if not selection:
                winner = match[0]
                loser = match[1]
            else:
                winner = match[1]
                loser = match[0]
            
            # Loser gets appended to the winning Team objects defeated_teams list
            winner.defeated_teams.append(loser)
            winners.append(winner)

def is_bracket_complete(teams, winners):
    # Function to check if the bracket has been finished playing out.
    
    # If teams list is exhausted and there is a single winner in winners list
    # then the bracket is complete
    return ('Bracket is complete!' if (len(teams) == 0 and len(winners) == 1) 
            else 'Bracket is incomplete!')

def find_champion(teams, winners):
    # Function to return the winner of the tournament

    return (f'Your champion is { winners[0] }' if len(teams) == 0 and 
            len(winners) == 1 else 'No champion yet! Play out the tournament!')

def champions_path_to_victory(winners):
    # Function that returns the champions defeated teams list in a f-string

    if len(winners) > 0:
        champion = winners[0]
    else:
        return('No champion!')

    champion_defeated_teams = [team.name for team in champion.defeated_teams]
    return (f'Your champion ({champion})\'s path of destruction is ' + 
            '-> '.join(champion_defeated_teams))

    
# Initial lists that we need.
teams = []
bracket = []
winners = []
teams = create_teams('teams.csv')
play_tournament(bracket, teams)

#print(len(winners))
#print(len(teams))
#print(winners[0].defeated_teams)
#print('Winner is ' + str(winners[-1]))
#print(f'Winner {winners[-1]} defeated ' + str(winners[-1].defeated_teams) + 
#       ' on their road to the championship!')

print(is_bracket_complete(teams, winners))
test_winners = []
print(is_bracket_complete(teams, test_winners))
test_teams = [Team(1, 'TEST SCHOOL')]
print(is_bracket_complete(test_teams, winners))
print(find_champion(teams, winners))
print(champions_path_to_victory(winners))
print(champions_path_to_victory(test_winners))