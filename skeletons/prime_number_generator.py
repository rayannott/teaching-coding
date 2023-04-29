def is_prime(n: int) -> bool:
    '''
    Checks if the natural number n is a prime.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---



def num_of_primes(a: int) -> int:
    '''
    Counts a number of primes among the values of f(x) = a * n^2 - 1
    for every n=0..99 and for a given fixed value of a.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


def find_first_best_a() -> int:
    '''
    Finds the smallest value of a such that num_of_primes(a) > 50
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


# TESTING (DO NOT MODIFY THIS BLOCK)
print('--- STARTED TESTING ---')
TEST_IS_PRIME = (
    [1,2,3,4,5,6,9,11,27,29],
    [False, True, True, False, True, False, False, True, False, True]
)
assert all(is_prime(num) == ans for num, ans in zip(*TEST_IS_PRIME)), 'is_prime failed'
print('is_prime passed')

TEST_NUM_OF_PRIMES = (
    [1,4,26,340],
    [1,1,24,13]
)
assert all(num_of_primes(num) == ans for num, ans in zip(*TEST_NUM_OF_PRIMES)), 'num_of_primes failed'
print('num_of_primes passed')
print('--- FINISHED TESTING ---')
# END OF TESTING

'''
Uncomment this to run the code
'''
# print(find_first_best_a())
