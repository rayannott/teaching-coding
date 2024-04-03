from brains import LinearListSearcher, BinarySearcher, Trie


def main():
    # brain = LinearListSearcher()
    brain = BinarySearcher()
    while True:
        inp = input('autocomplete> ')
        if not inp:
            break
        if inp.endswith('?'):
            print(inp[:-1] in brain)
        for word in brain.complete(inp):
            print('    -', word)


if __name__ == '__main__':
    main()
