'''
Global variables:
'''
# --- YOUR CODE HERE ---
DIGITS = {
    0: '1111110',
    1: '0110000',
    2: '1101101',
    3: '1111001',
    4: '0110011',
    5: '1011011',
    6: '1011111',
    7: '1110000',
    8: '1111111',
    9: '1111011'
}

# --- END OF YOUR CODE ---

def different_place_indices(bits1: str, bits2: str) -> list[int]:
    '''
    Return the list of indices at which two strings (with equal lengths) are not equal.
    '''
    # --- YOUR CODE HERE ---

    # --- END OF YOUR CODE ---


# TESTING
assert all(different_place_indices(*arg) == ans for arg, ans in zip(
        [('100', '110'), ('101001', '101001'), ('01101101010', '11111101100')], 
        [[1], [], [0,3,8,9]])
    ), 'different_place_indices failed'
print('different_place_indices passed')
# END OF TESTING


def potentially_displayed_digits(bits: str) -> list[tuple[int, str]]:
    '''
    Return a list of pairs: a number which can be displayed, a segment working incorrectly.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


'''
Uncomment this to run the code
'''
# TESTS = ['1101111', '1110001', '0110001', '0000011', '1111110']
# for t in TESTS:
#     print(t, potentially_displayed_digits(t))
