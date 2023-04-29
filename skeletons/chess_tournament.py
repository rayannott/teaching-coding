import os
from collections import defaultdict

Matches = list[tuple[str, str]]
PlayerMap = dict[str, str]
VicDefStatsDict = dict[str, list[int]]
VicDefStatsList = list[tuple[str, list[int]]]

def load_map() -> PlayerMap:
    FOLDER_NAME = 'files'; FILE_NAME = 'participants_map.txt'
    '''
    Load data and return a dictionary that maps hash to a name.
    '''
    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---

def load_matches() -> Matches:
    FOLDER_NAME = 'files'; FILE_NAME = 'games.txt'
    '''
    Load data and return a list of tuples of hashes: (person who won, person who lost)
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---

def count_victories_defeats(matches: Matches) -> VicDefStatsDict:
    '''
    Count victories and defeats of every player.
    Return dictionary objects which maps players hash 
        to a list of length 2: [number of victories, number of defeats]
    '''
    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---

def convert_to_vic_def_list(vic_def_dict: VicDefStatsDict) -> VicDefStatsList:
    '''
    (for later sorting)
    Return a list of items of an object returned by count_victories_defeats.
    '''
    return list(vic_def_dict.items())

def best_win_rate(vic_def: VicDefStatsList, player_map: PlayerMap) -> tuple[str, float]:
    '''
    Return a tuple
        (name of the player with the highest winrate, winrate as float)
    '''
    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---

def most_and_least_matches(vic_def: VicDefStatsList, player_map: PlayerMap):
    '''
    Return a tuple of two tuples a person with the most and the least amount of matches played: 
        ((name, most number of matches), (name, least number of matches))
    '''
    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---

def get_monicas_hash(player_map: PlayerMap) -> str:
    # Monica
    '''
    Return the hash of a player with a name 'Monica'
    '''
    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---

def get_monicas_performance(monicas_hash: str, vic_def_dict: VicDefStatsDict) -> tuple[int, int]:
    '''
    Return a tuple (Monica's victories, Monica's defeats).
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---

def get_monicas_defeaters(monicas_hash: str, matches: Matches, player_map: PlayerMap) -> list[str]:
    '''
    
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---



'''
Uncomment this to run the code
'''
# player_map = load_map()
# matches = load_matches()
# vic_def_dict = count_victories_defeats(matches)
# vic_def_list = convert_to_vic_def_list(vic_def_dict)
# best = best_win_rate(vic_def_list, player_map)
# most, least = most_and_least_matches(vic_def_list, player_map)
# print(f'best player: {best[0]} with {best[1]:.3%} winrate')
# print('most matches', *most)
# print('least matches', *least)
# monicas_hash = get_monicas_hash(player_map)
# monicas_perf = get_monicas_performance(monicas_hash, vic_def_dict)
# monicas_defeaters = get_monicas_defeaters(monicas_hash, matches, player_map)
# print('monicas_perf: %d wins and %d losses' % monicas_perf)
# print('defeaters:', ', '.join(monicas_defeaters))
