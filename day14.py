import math


def factorial(n):
    return math.factorial(n)


def lattice_paths(n):
    return factorial(2*n) // (factorial(n) * factorial(n))


# for 20 X 20 grid
print(lattice_paths(20))
