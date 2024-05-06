import pathlib


SMALL_FILE = pathlib.Path('downloads') / '5000-words.txt'
BIG_FILE = pathlib.Path('downloads') / '10000-words.txt'


def load_words(filepath: pathlib.Path) -> list[str]:
    with filepath.open() as file:
        return file.read().splitlines()


def word_reversed(word: str) -> str:
    return ''.join(reversed(word))


def get_reverse_pairs(words: list[str]) -> list[tuple[str, str]]:
    """
    Problem: "Reverse Pairs" 
    
    Given a list of words, find all pairs of words that are 
    reverses of each other.
    Skip duplicates.
    Skip palindromes.
    
    Example:
    ```python
    words = ['bat', 'cat', 'race', 'tab', 'tac', 'car', 'lol']
    assert get_reverse_pairs(words) == [('bat', 'tab'), ('cat', 'tac')]
    ```

    Requirements:
        - Time: O(n)
        - Space: O(n)
    """
    words_set = set(words)
    such_words = set()
    for w in words_set:
        rev = word_reversed(w)
        if w == rev:
            continue
        if rev in words_set and rev not in such_words:
            such_words.add(w)
    return [(w, word_reversed(w)) for w in such_words]


def main():
    # test:
    print(get_reverse_pairs(['bat', 'cat', 'race', 'tab', 'tac', 'car', 'lol']))

    # words from file:
    words = load_words(SMALL_FILE)
    pairs = get_reverse_pairs(words)
    print(pairs)


if __name__ == "__main__":
    main()
