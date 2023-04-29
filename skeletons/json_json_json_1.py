# SKELETON SOLUTION: minecraft stats (json json json 1)
import json, os

def read_json() -> dict:
    '''
    Reads the .json file and returns a dict object with the stats only (no DataVersion)
    '''
    # hint: use os.path.join
    
    to_return = {}
    FOLDER_NAME = 'files'; FILENAME = 'minecraft_stats.json'

    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---

    assert "minecraft:custom" in to_return and \
        "minecraft:picked_up" in to_return, \
        'Incorrect object: among others, it must have the keys minecraft:custom, minecraft:picked_up'
    
    return to_return


def remove_minecraft_colon(data: dict) -> dict:
    '''
    Removes the 'minecraft:' part from the beginning of all key strings
    '''
    res = {}

    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---

    assert 'custom' in res and 'climb_one_cm' in res['custom'], 'Something went wrong'

    return res


def min_max_stats(this_stats_data: dict) -> tuple[tuple[str, int], tuple[str, int]]:
    '''
    For inner dict[str, int] object returns a tuple ((key, min_value), (key, max_value)).
    For example, if this_stats_data is a dict under key 'mined', the function may return (('anvil', 1), ('dirt', 1244))
    '''
    min_ = (), max_ = ()

    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---

    return min_, max_


def display_stats(data: dict):
    '''
    For every stats category, except for 'custom', print the min_max_stats result in a readable form.
    '''
    # hint: Use min_max_stats here

    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---


'''
Uncomment this to run the code
'''
# data = read_json()
# data = remove_minecraft_colon(data)
# display_stats(data)
