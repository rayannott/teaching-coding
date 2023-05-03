'''
This skeleton file provides a basic intro to dict type in python.
Complete all functions by filling the gaps between YOUR CODE HERE and END OF YOUR CODE.
Running the script will test the functions one by one starting from the first.

Set the RAISE_ON_FAIL variable to True if you want the program to raise an exception when a test fails.
'''

RAISE_ON_FAIL = False

# --- YOUR CODE HERE ---

# --- END OF YOUR CODE ---



'--- PART 1: CREATION ---'

def init_1() -> dict[str, int]:
    '''
    Initialize a dictionary with the keys 'one', 'two' and 'three' having values 1, 2 and 3, respectively.
    Then return this dict object.
    '''
    # --- YOUR CODE HERE ---
    return {'one': 1, 'two': 2, 'three': 3}
    # --- END OF YOUR CODE ---
    

def init_2() -> dict[str, float]:
    '''
    Initialize a dictionary with keys from KEYS and values from VALUES.
    Then return this dict object.
    '''
    KEYS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    VALUES = [13.2, 5.4, 7.7, 0.0, 2.3, 5.2, 0.6]
    # --- YOUR CODE HERE ---
    return dict(zip(KEYS, VALUES))
    # --- END OF YOUR CODE ---


def init_3() -> dict[int, int]:
    '''
    Initialize a dictionary that maps a number to its square for the first
    12 natural numbers (KEYS).
    Then return this dict object.
    '''
    KEYS = range(1, 13)
    # --- YOUR CODE HERE ---
    return {k: k**2 for k in KEYS}
    # --- END OF YOUR CODE ---



'--- PART 2: ITERATION ---'

def iter_1(d: dict[int, int]) -> int:
    '''
    Return the difference between the sum of all keys and the sum of all values: sum(keys) - sum(values)
    '''
    # --- YOUR CODE HERE ---
    return sum(d.keys()) - sum(d.values())
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
    l = list(d.items())
    l.sort(key=lambda x: x[0])
    return l
    # --- END OF YOUR CODE ---


def iter_4(d: dict[int, str]) -> list[str]:
    '''
    Return a list of values corresponding to even keys.
    '''
    # --- YOUR CODE HERE ---
    return [v for k, v in d.items() if k % 2 == 0]
    # --- END OF YOUR CODE ---



'--- PART 3: MANIPULATION ---'

def manip_1(d: dict[int, int]) -> None:
    '''
    Increase every value with an odd key by 1.
    '''
    # --- YOUR CODE HERE ---
    for k in d:
        if k % 2 == 1:
            d[k] += 1
    # --- END OF YOUR CODE ---


def manip_2(d: dict) -> dict:
    '''
    Return a new dictionary where keys and values are swapped (<key>: <value> -> <value>: <key>).
    It is guaranteed that all values are unique. 
    '''
    # --- YOUR CODE HERE ---
    return dict(zip(d.values(), d.keys()))
    # --- END OF YOUR CODE ---


def manip_3(d: dict[int, int]) -> None:
    '''
    Insert missing integers between min(keys) and max(keys) with values all equal to 0
    '''
    # --- YOUR CODE HERE ---
    for k in range(min(d.keys())+1, max(d.keys())):
        if k not in d:
            d[k] = 0
    # --- END OF YOUR CODE ---


def manip_4(d: dict[int, int]) -> None:
    '''
    For every key-value pair insert (2*key, 2*value) if 2*key does not exist.
    '''
    # --- YOUR CODE HERE ---
    to_add = [(2*k, 2*v) for k, v in d.items() if 2*k not in d]
    d.update(to_add)
    # --- END OF YOUR CODE ---



'--- PART 4: OTHER ---'

def oth_1(d):
    '''
    
    '''
    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---


def oth_2(d):
    '''
    
    '''
    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---


def oth_3(d):
    '''
    
    '''
    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---




# ----------------- <TESTS> -----------------
def test_init_1():
    d = init_1()
    return d['one'] == 1 and d['two'] == 2 and d['three'] == 3 and len(d) == 3

def test_init_2():
    d = init_2()
    for k, v in zip(['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                    [13.2, 5.4, 7.7, 0.0, 2.3, 5.2, 0.6]):
        if d[k] != v: return False
    return True and len(d) == 7

def test_init_3():
    d = init_3()
    return set(d.keys()) == set(range(1, 13)) and all(map(lambda x: x[0]**2 == x[1], d.items()))

def test_iter_1():
    return iter_1({1: 3, 2: 5}) == -5 and \
            iter_1({3: 2, 4: 5, 6: 3, 9: 0}) == 12 and \
            iter_1({1: 1}) == 0

def test_iter_3():
    d1 = {1: 5, 4: -1, 6: 3, 0: 1}
    d2 = {4: 1, 3: 2, 2: 3, 1: 4}
    d3 = {0: 0, 2: -100, -2: 100}
    return iter_3(d1) == [(0, 1), (1, 5), (4, -1), (6, 3)] and \
            iter_3(d2) == [(1, 4), (2, 3), (3, 2), (4, 1)] and \
            iter_3(d3) == [(-2, 100), (0, 0), (2, -100)]

def test_iter_4():
    d1 = {1: 5, 4: -1, 6: 3, 0: 1}
    d2 = {4: 1, 3: 2, 2: 3, 1: 4}
    d3 = {0: 0, 2: -100, -2: 100}
    d4 = {1: 4, 3: -5}
    d5 = {2: 1, -6: 3}
    return iter_4(d1) == [-1, 3, 1] and \
            iter_4(d2) == [1, 3] and \
            iter_4(d3) == [0, -100, 100] and \
            iter_4(d4) == [] and \
            iter_4(d5) == [1, 3]

def test_manip_1():
    d1 = {1: 5, 4: -1, 6: 3, 0: 1}
    d2 = {4: 1, 3: 2, 2: 3, 1: 4}
    d3 = {0: 0, 2: -100, -2: 100}
    d4 = {1: 4, 3: -5}
    d5 = {2: 1, -6: 3}
    manip_1(d1); manip_1(d2)
    manip_1(d3); manip_1(d4); manip_1(d5)
    return d1 == {1: 6, 4: -1, 6: 3, 0: 1} and \
            d2 == {4: 1, 3: 3, 2: 3, 1: 5} and \
            d3 == {0: 0, 2: -100, -2: 100} and \
            d4 == {1: 5, 3: -4} and \
            d5 == {2: 1, -6: 3}

def test_manip_2():
    d1 = {1: 5, 4: -1, 6: 3, 0: 1}
    d2 = {4: 1, 3: 2, 2: 3, 1: 4}
    d3 = {0: 0, 2: -100, -2: 100}
    d4 = {1: 4, 3: -5}
    d5 = {2: 1, -6: 3}
    return manip_2(d1) == {5: 1, -1: 4, 3: 6, 1: 0} and \
            manip_2(d2) == {1: 4, 2: 3, 3: 2, 4: 1} and \
            manip_2(d3) == {0: 0, -100: 2, 100: -2} and \
            manip_2(d4) == {4: 1, -5: 3} and \
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
    return d1 == {1: 5, 4: -1, 6: 3, 0: 1, 2: 0, 3: 0, 5: 0} and \
            d2 == {4: 1, 3: 2, 2: 3, 1: 4} and \
            d3 == {0: 0, 2: -100, -2: 100, -1: 0, 1: 0} and \
            d4 == {1: 4, 3: -5, 2: 0} and \
            d5 == {2: 1, -6: 3, -5: 0, -4: 0, -3: 0, -2: 0, -1: 0, 0: 0, 1: 0}

def test_manip_4():
    d2 = {1: 2, 3: 4, 5: 6}
    d3 = {0: 2, 1: 5, 2: 7}
    d4 = {1: 4, 3: -5}
    manip_4(d4)
    manip_4(d3)
    manip_4(d2)
    return d4 == {1: 4, 3: -5, 2: 8, 6: -10} and \
            d3 == {0: 2, 1: 5, 2: 7, 4: 14} and \
            d2 == {1: 2, 3: 4, 5: 6, 2: 4, 6: 8, 10: 12}


TESTS = [
    test_init_1, test_init_2, test_init_3,
    test_iter_1, test_iter_3, test_iter_4,
    test_manip_1, test_manip_2, test_manip_3, test_manip_4

]

def test():
    passed = 0
    for i, test_func in enumerate(TESTS):
        print(f'{i}. testing [{test_func.__name__}]...')
        if not test_func():
            msg = f'[{test_func.__name__}] FAILED ' + '-'*15
            if RAISE_ON_FAIL:
                raise AssertionError(msg)
            else:
                print(msg)
        else:
            print(f'[{test_func.__name__}] passed')
            passed += 1
    if passed == len(TESTS):
        print('--- ALL PASSED ---')
    else:
        print(f'--- {passed}/{len(TESTS)} PASSED ---')



# ---------------- </TESTS> -----------------


if __name__ == '__main__':
    test()
