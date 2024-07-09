import random
from dataclasses import dataclass
from itertools import pairwise
from collections import defaultdict


@dataclass
class Song:
    id: int
    type: int


def violations(songs: list[Song]) -> int:
    return sum(s1.type == s2.type for s1, s2 in pairwise(songs))


def shuffled(songs: list[Song]) -> list[Song]:
    """
    Returns a new list where the songs are shuffled pseudorandomly.
    That is, the number of adjacent song pairs with the same type is minimized:
        >>> from itertools import pairwise
        >>> songs_shuffled = shuffled(songs)
        >>> # the following value is as small as possible for a given list of songs
        >>> num_violations = violations(songs_shuffled)

    And the uniformity is not violated: each song has an equal probability
    to appear at any place in the shuffled list.
    """
    ...
