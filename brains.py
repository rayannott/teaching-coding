import pathlib
from abc import ABC, abstractmethod


WORDS_FILE = pathlib.Path('words_most_common.txt')
WORDS = WORDS_FILE.read_text().splitlines()
WORDS = [word for word in WORDS if len(word) > 2]


class Autocompleter(ABC):
    @abstractmethod
    def complete(self, prefix: str) -> list:
        pass

    @abstractmethod
    def __contains__(self, word: str) -> bool:
        pass


class LinearListSearcher(Autocompleter):
    def __init__(self):
        self.words = WORDS
    
    def complete(self, prefix: str) -> list:
        return [word for word in self.words if word.startswith(prefix)]

    def __contains__(self, word: str) -> bool:
        return word in self.words


class LinearSetSearcher(Autocompleter):
    def __init__(self):
        self.words = set(WORDS)
    
    def complete(self, prefix: str) -> list:
        return [word for word in self.words if word.startswith(prefix)]

    def __contains__(self, word: str) -> bool:
        return word in self.words

class BinarySearcher(Autocompleter):
    def __init__(self):
        self.words = sorted(WORDS)
    
    def __contains__(self, word: str) -> bool:
        return self._binary_search_index(word)[0]

    def complete(self, prefix: str) -> list:
        start_idx = self._binary_search_index(prefix)[1]
        res = []
        # try to optimize this using indexing, without slicing
        for word in self.words[start_idx:]:
            if not word.startswith(prefix):
                break
            res.append(word)
        return res
    
    def _binary_search_index(self, word: str) -> tuple[bool, int]:
        """
        Returns:
        - True if the word is found in the list of words; False otherwise.
        - the index of the word in the sorted list of words; if the word is not found, returns the index where the word would be inserted.

        E.g.:
        words = ['apple', 'banana', 'cherry']
        _binary_search_index('banana') -> True, 1
        _binary_search_index('cherry') -> True, 2
        _binary_search_index('mango') -> False, 3 # 'mango' would be inserted at index 3
        _binary_search_index('apricot') -> False, 1 # 'apricot' would be inserted at index 1
        """
        left, right = 0, len(self.words) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.words[mid] == word:
                return True, mid
            if self.words[mid] < word:
                left = mid + 1
            else:
                right = mid - 1
        return False, left


class Trie(Autocompleter):
    class _Node:
        def __init__(self):
            self.children: dict[str, Trie._Node] = {}
            self.is_word = False
    
    def __init__(self):
        ...
    
    def __contains__(self, word: str) -> bool:
        ...

    def complete(self, prefix: str) -> list:
        ...


if __name__ == '__main__':
    brain = BinarySearcher()
    while True:
        inp = input('>>> ')
        if not inp:
            break
        print(brain._binary_search_index(inp))
        