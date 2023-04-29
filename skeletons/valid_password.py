from string import ascii_uppercase

'''
Global variables (optional):
'''
# --- YOUR CODE HERE ---

# --- END OF YOUR CODE ---


def passes_length(password: str) -> bool:
    '''
    Checks the 1st condition.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def passes_capital_chars(password: str) -> bool:
    '''
    Checks the 2nd condition.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def passes_special_symbols(password: str) -> bool:
    '''
    Checks the 3rd condition.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def passes_digits(password: str) -> bool:
    '''
    Checks the 4th condition.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def is_valid_password(password: str) -> bool:
    '''
    The password is valid if at least 3 of the 4 following conditions are true:
    1. len >= 10
    2. at least two capital letters
    3. at least one special symbol from !-+/*&%$#_@()[]
    4. at least three digits
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---
    

# TESTING
print('--- STARTED TESTING ---')
assert all(passes_length(pwd) == ans for pwd, ans in zip(
        ['acd748ghc', '1yd758gja1', '473hdjqudhfgn'], 
        [False, True, True])
    ), 'passes_length failed'
print('passes_length passed')

assert all(passes_special_symbols(pwd) == ans for pwd, ans in zip(
        ['acd8ghc', '1yd7_Bgja1', '$', '7f!67@2G'], 
        [False, True, True, True])
    ), 'passes_special_symbols failed'
print('passes_special_symbols passed')

assert all(passes_capital_chars(pwd) == ans for pwd, ans in zip(
        ['acd7#$48ghc', '1yd7_Bgja1', 'aqwBqsgF_', '7f67AiBiu2G'], 
        [False, False, True, True])
    ), 'passes_capital_chars failed'
print('passes_capital_chars passed')

assert all(passes_digits(pwd) == ans for pwd, ans in zip(
        ['acd7#$ghc', '1yd_Bgja', 'aqw2Bqs5gF_', '7f67AiBiu2G', 'hjshgdf7hg16ghd6'], 
        [False, False, False, True, True])
    ), 'passes_digits failed'
print('passes_digits passed')
print('--- FINISHED TESTING ---')
# END OF TESTING


'''
Uncomment this to run the code
'''
# TESTS = ['iuhkQe82jGa', 'Aiq3uyf3G1', 'ruQ-1d4G', 'qkqFDuQh4FG3FG', '2$A48bc753']
# for t in TESTS:
#     print(t, is_valid_password(t))
