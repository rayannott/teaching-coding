import timeit
from string import ascii_lowercase
import random
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

random.seed(0)
_SUBSET = random.sample(WORDS, 1000)
_MISSING_WORDS = [
    wrd
    for _ in range(1000)
    if (wrd:=''.join(random.choices(ascii_lowercase, k=random.randint(2, 6)))) not in WORDS
]
_PREFIXES = [w[:random.randint(2, 5)] for w in random.sample(WORDS, 100)]


def test_correctness(autocompleter_cls: Type[Autocompleter]) -> None:
    autocompleter = autocompleter_cls()
    def _contains():
        for word in _SUBSET:
            assert word in autocompleter, f'{word} not found by {autocompleter_cls.__name__}'
        for word in _MISSING_WORDS:
            assert word not in autocompleter, f'{word} found by {autocompleter_cls.__name__}'
    def _complete():
        TESTS = [
            ('qy', set()),
            ('_', set()),
            ('requi', {'require', 'required', 'requirement', 'requirements', 'requires', 'requiring'}),
            ('aba', {'abandoned'}),
            ('lis', {'lisa', 'list', 'listed', 'listen', 'listening', 'listing', 'listings', 'listprice', 'lists'}),
            ('tota', {'total', 'totally', 'totals'}),
        ]
        for prefix, expected in TESTS:
            assert (output:=set(autocompleter.complete(prefix))) == expected, \
                f'failed for {prefix} in {autocompleter_cls.__name__}: {output!r} != {expected!r}'
    print(f'testing {autocompleter_cls.__name__}...')
    _contains()
    print(f'- [contains] {autocompleter_cls.__name__:<20}: OK')
    _complete()
    print(f'- [complete] {autocompleter_cls.__name__:<20}: OK')


def time_init(autocompleter_cls: Type[Autocompleter]) -> tuple[float, float]:
    N = 500
    times = timeit.repeat(
        stmt=f'autocompleter_cls()',
        globals={'autocompleter_cls': autocompleter_cls},
        repeat=5,
        number=N
    )
    return mean(times) / N, stdev(times) / N


def time_contains(autocompleter_cls: Type[Autocompleter]) -> tuple[float, float]:
    N = 300
    times = timeit.repeat(
        stmt='for word in _SUBSET: word in autocompleter',
        globals={'_SUBSET': _SUBSET, 'autocompleter_cls': autocompleter_cls,},
        setup='autocompleter = autocompleter_cls()',
        repeat=5,
        number=N
    )
    return mean(times) / N, stdev(times) / N


def time_complete(autocompleter_cls: Type[Autocompleter]) -> tuple[float, float]:
    N = 300
    times = timeit.repeat(
        stmt='for prefix in _PREFIXES: autocompleter.complete(prefix)',
        globals={'_PREFIXES': _PREFIXES, 'autocompleter_cls': autocompleter_cls},
        setup='autocompleter = autocompleter_cls()',
        repeat=5,
        number=N
    )
    return mean(times) / N, stdev(times) / N


def main():
    for cls in (
        LinearListSearcher,
        LinearSetSearcher,
        BinarySearcher,
        Trie
    ):
        # run correctness test
        test_correctness(cls)

        print(f'benchmarking {cls.__name__}...')
        # benchmark `__init__`
        mean_time, stdev_time = time_init(cls)
        print(f'- [init] {cls.__name__}: {mean_time:e} ± {stdev_time:e} seconds')

        # benchmark `__contains__`
        mean_time, stdev_time = time_contains(cls)
        print(f'- [contains] {cls.__name__}: {mean_time:e} ± {stdev_time:e} seconds')

        # benchmark `complete`
        mean_time, stdev_time = time_complete(cls)
        print(f'- [complete] {cls.__name__}: {mean_time:e} ± {stdev_time:e} seconds')
        print()


if __name__ == '__main__':
    main()


OUTPUT = '''
testing LinearListSearcher...
- [contains] LinearListSearcher  : OK
- [complete] LinearListSearcher  : OK
benchmarking LinearListSearcher...
- [init] LinearListSearcher: 6.580000e-08 ± 1.777640e-09 seconds
- [contains] LinearListSearcher: 1.912312e-02 ± 9.173350e-05 seconds
- [complete] LinearListSearcher: 3.407880e-02 ± 1.037238e-04 seconds

testing LinearSetSearcher...
- [contains] LinearSetSearcher   : OK
- [complete] LinearSetSearcher   : OK
benchmarking LinearSetSearcher...
- [init] LinearSetSearcher: 3.214508e-04 ± 5.228150e-05 seconds
- [contains] LinearSetSearcher: 4.422753e-05 ± 1.263165e-06 seconds
- [complete] LinearSetSearcher: 4.442390e-02 ± 3.321845e-04 seconds

testing BinarySearcher...
- [contains] BinarySearcher      : OK
- [complete] BinarySearcher      : OK
benchmarking BinarySearcher...
- [init] BinarySearcher: 1.352829e-03 ± 1.698661e-05 seconds
- [contains] BinarySearcher: 1.078434e-03 ± 1.416666e-05 seconds
- [complete] BinarySearcher: 1.235397e-03 ± 2.797821e-05 seconds

testing Trie...
- [contains] Trie                : OK
- [complete] Trie                : OK
benchmarking Trie...
- [init] Trie: 1.361904e-02 ± 4.185760e-04 seconds
- [contains] Trie: 7.356163e-04 ± 2.864143e-05 seconds
- [complete] Trie: 2.960551e-03 ± 1.258089e-05 seconds
'''
