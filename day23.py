from itertools import permutations


def lexicographic(n, digits):
    """Assumes digits a string.
    returns the nth item of the lexicographic permutation of digits."""
    return list(permutations(digits))[n - 1]


if __name__ == '__main__':
    permutation = list(lexicographic(1000000, '0123456789'))
    print(''.join(permutation))
