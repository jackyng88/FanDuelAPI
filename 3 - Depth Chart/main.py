'''
    {
        player_id: 1,
        name: "Bob",
        position: “WR”
    }

'''

class Player():

    def __init__(self, id, name, position):
        self.player_id = id
        self.name = name
        self.position = position

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.player_id)

# Depth chart is a dictionray that will eventually become a dictionary of 
# positions of which will be a list of player objects. For example, 
# depth_chart = {'WR': [PlayerObject1, PlayerObject2], 'QB': [PlayerObject3]}
depth_chart = {}
new_player = Player(1, 'Mike', 'WR')
new_player_2 = Player (2, 'John', 'WR')
new_player_3 = Player (3, 'Sean', 'QB')
new_player_4 = Player (4, 'Andy', 'WR')

def	addPlayerToDepthChart(player, position, position_depth=None):
    # Function to add player to depth chart.

    if position not in depth_chart:
        depth_chart[position] = []
        depth_chart[position].append(player)
    
    else:
        if position_depth is None:
            depth_chart[position].append(player)
        else:
            depth_chart[position].insert(position_depth, player)

def	removePlayerFromDepthChart(player, position):
    # Function to remove player from depth chart.
    if depth_chart.get(position):
        # Position found in depth chart dictionary
        if player in depth_chart[position]:
            depth_chart[position].remove(player)
        else:
            print(f'{player} does not exist in this position\'s chart!')

    elif depth_chart.get(position):
        print('Position doesn\'t exist!')

def	getFullDepthChart():
    # Function to print out all the positions in the depth chart, returns
    # a tuple of the position and a list of the player IDs.

    #return list(depth_chart.items())
    all_players = [(pos,[player.name for player in players])
                    for pos, players in depth_chart.items()]

    return all_players

def	getPlayersUnderPlayerInDepthChart(player, position):
    # Function that returns all the players lower than the given player.

    players_under = []
    player_idx = 0
    end_idx = 0
    if depth_chart[position]:
        if player in depth_chart[position]:
            player_idx = depth_chart[position].index(player)
            end_idx = len(depth_chart[position]) 
            
    # players_under becomes a slice of the retrieved list that starts at one
    # value larger than the index for the player until the end of the list.
    players_under = depth_chart.get(position)[player_idx + 1:end_idx]
    return players_under



addPlayerToDepthChart(new_player, 'WR', 1)
addPlayerToDepthChart(new_player_2, 'WR', 1)
addPlayerToDepthChart(new_player_3, 'QB')
removePlayerFromDepthChart(new_player_3, 'WR')
addPlayerToDepthChart(new_player_4, 'WR')
print(getFullDepthChart())
print (getPlayersUnderPlayerInDepthChart(new_player, 'WR'))
#print(depth_chart.items())


for player_list in depth_chart.values():
    for player in player_list:
        print(str(player.player_id) + ' ' + player.name)

