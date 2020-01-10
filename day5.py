def sum_of_squares(n):
    return (n*(n+1)*(2*n+1)) // 6


def square_sum_of_sequence(n):
    return (n*(n+1) // 2)**2


print(square_sum_of_sequence(100) - sum_of_squares(100))

