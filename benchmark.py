import timeit
from statistics import mean, stdev
from typing import Type
from brains import (
    Autocompleter,
    LinearListSearcher,
    LinearSetSearcher,
    BinarySearcher,
    Trie,
    WORDS
)


def time_init(autocompleter_cls: Type[Autocompleter]) -> tuple[float, float]:
    N = 1000
    times = timeit.repeat(
        stmt=f'autocompleter_cls()',
        globals={'WORDS': WORDS, 'autocompleter_cls': autocompleter_cls},
        repeat=5,
        number=N
    )
    return mean(times) / N, stdev(times) / N


if __name__ == '__main__':
    for cls in (
        LinearListSearcher,
        LinearSetSearcher,
        BinarySearcher,
        Trie
    ):
        mean_time, stdev_time = time_init(cls)
        print(f'[init] {cls.__name__}: {mean_time:e} ± {stdev_time:e} seconds')
