from collections import defaultdict
import os


def load_tosses() -> list[int]:
    FOLDER_NAME = 'files'; FILENAME = 'tosses.txt'
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def count_streaks(tosses: list[int]) -> dict[int, int]:
    '''
    Counts the number of streaks (same consecutive numbers) and return a dictionary length: number_of_streaks
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


'''
Uncomment this to run the tests on the count_streaks function
'''
# TESTS = [
#     [1, 0, 1, 0, 1],
#     [1, 1, 0, 1, 0, 0, 0, 1, 1],
#     [1, 1, 1],
#     [1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
#     [1],
#     [0, 1, 1]
# ]
# ANS = [
#     {1: 5},
#     {2: 2, 1: 2, 3: 1},
#     {3: 1},
#     {1: 3, 2: 2, 3: 1},
#     {1: 1},
#     {1: 1, 2: 1}
# ]
# for t, ans in zip(TESTS, ANS):
#     cs = count_streaks(t)
#     print(f'{t} {cs}, {cs == ans}')


'''
Uncomment this to run the code on the experiment data and print the result
'''
# tosses = load_tosses()
# res = count_streaks(tosses)
# for data in sorted(res.items(), key=lambda x: x[0]):
#     print(data)


def _plot(res: dict[int, int]):
    from matplotlib import pyplot as plt
    import numpy as np
    n, S_n = zip(*sorted(res.items(), key=lambda x: x[0]))
    n_arr = np.array(n)
    S_n_arr = np.array(S_n)
    S_n_arr_log = np.log(S_n_arr)
    k, b = np.polyfit(n_arr, S_n_arr_log, deg=1)
    S_n_arr_fit = np.exp(b + k*n_arr)
    plt.plot(n_arr, S_n_arr, '.:')
    plt.plot(n_arr, S_n_arr_fit)
    plt.yscale('log')
    plt.xticks(n_arr)
    plt.grid()
    plt.show()


'''
If the experiment data works, uncomment this to create a plot
'''
# _plot(res)
