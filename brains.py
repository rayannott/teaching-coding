import pathlib
from abc import ABC, abstractmethod


WORDS_FILE = pathlib.Path('words_most_common.txt')
WORDS = WORDS_FILE.read_text().splitlines()
WORDS = [word for word in WORDS if len(word) > 2]


from abc import ABC, abstractmethod

class Autocompleter(ABC):
    """
    An abstract base class for autocompleter implementations.
    """

    @abstractmethod
    def complete(self, prefix: str) -> list:
        """
        Returns a list of completions for the given prefix.

        Args:
            prefix (str): The prefix to be completed.

        Returns:
            list: A list of completions for the given prefix.

        E.g.:
        >>> WORDS = ['apple', 'apricot', 'aloe', 'cherry', 'date', 'fig', 'grape']
        >>> autocompleter = Autocompleter() # WORDS is a global variable
        >>> autocompleter.complete('ap')
        ['apple', 'apricot']
        """
        pass

    @abstractmethod
    def __contains__(self, word: str) -> bool:
        """
        Checks if the autocompleter contains the given word.

        Args:
            word (str): The word to be checked.

        Returns:
            bool: True if the autocompleter contains the word, False otherwise.
        
        E.g.:
        >>> WORDS = ['apple', 'apricot', 'aloe', 'cherry', 'date', 'fig', 'grape']
        >>> autocompleter = Autocompleter() # WORDS is a global variable
        >>> 'apple' in autocompleter
        True
        >>> 'banana' in autocompleter
        False
        """
        pass


class LinearListSearcher(Autocompleter):
    def __init__(self):
        ...
    
    def complete(self, prefix: str) -> list:
        ...

    def __contains__(self, word: str) -> bool:
        ...


class LinearSetSearcher(Autocompleter):
    def __init__(self):
        ...
    
    def complete(self, prefix: str) -> list:
        ...

    def __contains__(self, word: str) -> bool:
        ...


class BinarySearcher(Autocompleter):
    def __init__(self):
        ...
    
    def __contains__(self, word: str) -> bool:
        ...

    def complete(self, prefix: str) -> list:
        ...


class Trie(Autocompleter):
    def __init__(self):
        ...
    
    def __contains__(self, word: str) -> bool:
        ...

    def complete(self, prefix: str) -> list:
        ...
