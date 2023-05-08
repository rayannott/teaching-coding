'''
This skeleton file provides a basic intro to dict type in python.
Complete all functions by filling the gaps between YOUR CODE HERE and END OF YOUR CODE.
Running the script will test the functions one by one starting from the first.

Set the RAISE_ON_FAIL variable to True if you want the program to raise an exception when a test fails.
Set the RUN_TESTS to False if you don't wont to run the tests on every run of the script.
'''

RAISE_ON_FAIL = False
RUN_TESTS = True



'--- PART 1: CREATION ---'

def init_1() -> dict[str, int]:
    '''
    Initialize a dictionary with the keys 'one', 'two' and 'three' having values 1, 2 and 3, respectively.
    Then return this dict object.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---
    

def init_2() -> dict[str, float]:
    '''
    Initialize a dictionary with keys from KEYS and values from VALUES.
    Then return this dict object.
    '''
    KEYS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    VALUES = [13.2, 5.4, 7.7, 0.0, 2.3, 5.2, 0.6]
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def init_3() -> dict[int, int]:
    '''
    Initialize a dictionary that maps a number to its square for the first
    12 natural numbers (KEYS).
    Then return this dict object.
    '''
    KEYS = range(1, 13)
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---



'--- PART 2: ITERATION ---'

def iter_1(d: dict[int, int]) -> int:
    '''
    Return the difference between the sum of all keys and the sum of all values: sum(keys) - sum(values)
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def iter_2(d: dict[int, int]):
    '''
    For every key-value pair of a given dict print "<key> -> <value>"
    '''
    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---


def iter_3(d: dict[int, int]) -> list[tuple[int, int]]:
    '''
    Return a list or pairs (key, value) of a given dict sorted by <key> (ascending).
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def iter_4(d: dict[int, str]) -> list[str]:
    '''
    Return a list of values corresponding to even keys.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---



'--- PART 3: MANIPULATION ---'

def manip_1(d: dict[int, int]) -> None:
    '''
    Increase every value with an odd key by 1.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def manip_2(d: dict) -> dict:
    '''
    Return a new dictionary where keys and values are swapped (<key>: <value> -> <value>: <key>).
    It is guaranteed that all values are unique. 
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def manip_3(d: dict[int, int]) -> None:
    '''
    Insert missing integers between min(keys) and max(keys) with values all equal to 0
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def manip_4(d: dict[int, int]) -> None:
    '''
    For every key-value pair insert (2*key, 2*value) if 2*key does not exist.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---



'--- PART 4: OTHER ---'

def oth_1(d1: dict[int, int], d2: dict[int, int]) -> bool:
    '''
    Return a union of two dicts. That is, a new dictionary with key-value pairs from both.
    It is guaranteed that d1 and d2 have different sets of keys: d1.keys() & d2.keys() == set().
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def oth_2(text: str) -> str:
    '''
    Given a string of text consisting of lowercase english letters,
    return a new string where every letter is replaced with
    its number in the alphabet: a -> 1, b -> 2, ..., z -> 26.
    Ex.: 'aaabbc' -> '111223', 'hello' -> '85121215'.
    '''
    from string import ascii_lowercase
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def oth_3(d: dict[str, list[int]], door_number: int) -> list[str]:
    '''
    Given a dictionary which maps a password to a list of doors that can be opened with it
    and a door number,
    return a list of passwords that can be used to open the door.
    Return result in any order.
    Ex.: for {'ab': [4, 6], 'c': [3, 4], 'd': [3, 1, 5], 'e': [3, 5, 4]}
        and door_number = 4 the answer is ['ab', 'c', 'e']
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---



# ----------------- <TESTS> -----------------
def test_init_1():
    d = init_1()
    return d['one'] == 1, d['two'] == 2, d['three'] == 3, len(d) == 3

def test_init_2():
    d = init_2()
    res = []
    for k, v in zip(['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                    [13.2, 5.4, 7.7, 0.0, 2.3, 5.2, 0.6]):
        res.append(d[k] == v)
    res.append(len(d) == 7)
    return res

def test_init_3():
    d = init_3()
    return set(d.keys()) == set(range(1, 13)), all(map(lambda x: x[0]**2 == x[1], d.items()))

def test_iter_1():
    return iter_1({1: 3, 2: 5}) == -5, \
            iter_1({3: 2, 4: 5, 6: 3, 9: 0}) == 12, \
            iter_1({1: 1}) == 0

def test_iter_3():
    d1 = {1: 5, 4: -1, 6: 3, 0: 1}
    d2 = {4: 1, 3: 2, 2: 3, 1: 4}
    d3 = {0: 0, 2: -100, -2: 100}
    return iter_3(d1) == [(0, 1), (1, 5), (4, -1), (6, 3)], \
            iter_3(d2) == [(1, 4), (2, 3), (3, 2), (4, 1)], \
            iter_3(d3) == [(-2, 100), (0, 0), (2, -100)]

def test_iter_4():
    d1 = {1: 5, 4: -1, 6: 3, 0: 1}
    d2 = {4: 1, 3: 2, 2: 3, 1: 4}
    d3 = {0: 0, 2: -100, -2: 100}
    d4 = {1: 4, 3: -5}
    d5 = {2: 1, -6: 3}
    return iter_4(d1) == [-1, 3, 1], \
            iter_4(d2) == [1, 3], \
            iter_4(d3) == [0, -100, 100], \
            iter_4(d4) == [], \
            iter_4(d5) == [1, 3]

def test_manip_1():
    d1 = {1: 5, 4: -1, 6: 3, 0: 1}
    d2 = {4: 1, 3: 2, 2: 3, 1: 4}
    d3 = {0: 0, 2: -100, -2: 100}
    d4 = {1: 4, 3: -5}
    d5 = {2: 1, -6: 3}
    manip_1(d1); manip_1(d2)
    manip_1(d3); manip_1(d4); manip_1(d5)
    return d1 == {1: 6, 4: -1, 6: 3, 0: 1}, \
            d2 == {4: 1, 3: 3, 2: 3, 1: 5}, \
            d3 == {0: 0, 2: -100, -2: 100}, \
            d4 == {1: 5, 3: -4}, \
            d5 == {2: 1, -6: 3}

def test_manip_2():
    d1 = {1: 5, 4: -1, 6: 3, 0: 1}
    d2 = {4: 1, 3: 2, 2: 3, 1: 4}
    d3 = {0: 0, 2: -100, -2: 100}
    d4 = {1: 4, 3: -5}
    d5 = {2: 1, -6: 3}
    return manip_2(d1) == {5: 1, -1: 4, 3: 6, 1: 0}, \
            manip_2(d2) == {1: 4, 2: 3, 3: 2, 4: 1}, \
            manip_2(d3) == {0: 0, -100: 2, 100: -2}, \
            manip_2(d4) == {4: 1, -5: 3}, \
            manip_2(d5) == {1: 2, 3: -6}

def test_manip_3():
    d1 = {1: 5, 4: -1, 6: 3, 0: 1}
    d2 = {4: 1, 3: 2, 2: 3, 1: 4}
    d3 = {0: 0, 2: -100, -2: 100}
    d4 = {1: 4, 3: -5}
    d5 = {2: 1, -6: 3}
    manip_3(d1)
    manip_3(d2)
    manip_3(d3)
    manip_3(d4)
    manip_3(d5)
    return d1 == {1: 5, 4: -1, 6: 3, 0: 1, 2: 0, 3: 0, 5: 0}, \
            d2 == {4: 1, 3: 2, 2: 3, 1: 4}, \
            d3 == {0: 0, 2: -100, -2: 100, -1: 0, 1: 0}, \
            d4 == {1: 4, 3: -5, 2: 0}, \
            d5 == {2: 1, -6: 3, -5: 0, -4: 0, -3: 0, -2: 0, -1: 0, 0: 0, 1: 0}

def test_manip_4():
    d2 = {1: 2, 3: 4, 5: 6}
    d3 = {0: 2, 1: 5, 2: 7}
    d4 = {1: 4, 3: -5}
    manip_4(d4)
    manip_4(d3)
    manip_4(d2)
    return d4 == {1: 4, 3: -5, 2: 8, 6: -10}, \
            d3 == {0: 2, 1: 5, 2: 7, 4: 14}, \
            d2 == {1: 2, 3: 4, 5: 6, 2: 4, 6: 8, 10: 12}

def test_oth_1():
    d11 = {1: 4, 3: 7}; d12 = {2: 8, 9: 10}
    d21 = {0: 4}; d22 = {4: 0}
    d31 = {1: 4}; d32 = {}
    return oth_1(d11, d12) == {1: 4, 3: 7, 2: 8, 9: 10}, \
            oth_1(d21, d22) == {0: 4, 4: 0}, \
            oth_1(d31, d32) == {1: 4}

def test_oth_2():
    return oth_2('ok') == '1511', \
            oth_2('zbaqd') == '2621174', \
            oth_2('wyghaw') == '232578123', \
            oth_2('qdhjakd') == '1748101114', \
            oth_2('pozlqf') == '16152612176', \
            oth_2('ghuiszbxcnbnz') == '78219192622431421426', \
            oth_2('a') == '1', \
            oth_2('z') == '26'
    
def test_oth_3():
    def _eq_sets(l1, l2):
        return set(l1) == set(l2)
    d1 = {'ab': [4, 6], 'c': [3, 4], 'd': [3, 1, 5], 'e': [3, 5, 4]}
    d2 = {'a': [1, 5], 'b': [3, 6], 'c': [4, 1]}
    return _eq_sets(oth_3(d1, 4), ['ab', 'c', 'e']), \
            _eq_sets(oth_3(d2, 7), []), \
            _eq_sets(oth_3(d1, 5), ['d', 'e']), \
            _eq_sets(oth_3(d2, 3), ['b'])


TESTS = [
    test_init_1, test_init_2, test_init_3,
    test_iter_1, test_iter_3, test_iter_4,
    test_manip_1, test_manip_2, test_manip_3, test_manip_4,
    test_oth_1, test_oth_2, test_oth_3
]

def test():
    passed = 0
    for i, test_func in enumerate(TESTS):
        print(f'{i}. testing [{test_func.__name__[5:]}]...', end=' ')
        try:
            test_result = test_func()
        except Exception as e:
            print(f'[{test_func.__name__[5:]}] FAILED with an exception: {e}')
        else:
            if not all(test_result):
                msg = f'[{test_func.__name__[5:]}] FAILED: passed only {sum(test_result)}/{len(test_result)}' + '-'*15
                if RAISE_ON_FAIL:
                    raise AssertionError(msg)
                else:
                    print(msg)
            else:
                print(f'[{test_func.__name__[5:]}] passed {sum(test_result)}/{len(test_result)}')
                passed += 1
    if passed == len(TESTS):
        print('--- ALL PASSED ---')
    else:
        print(f'--- {passed}/{len(TESTS)} PASSED ---')



# ---------------- </TESTS> -----------------


if __name__ == '__main__':
    # --- A PLACE TO WRITE YOUR OWN TESTS ---


    # ---------------------------------------
    if RUN_TESTS:
        test()
