from math import *


def divisors(n):
    limit = int(sqrt(n))
    divisors_list = []
    for i in range(1, limit + 1, 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n / i:
                divisors_list.append(n / i)
    return len(divisors_list)


def is_triangle_number(n):
    a = int(sqrt(2 * n))
    return 0.5 * a * (a + 1) == n


def last_term(n):
    if is_triangle_number(n):
        return int(sqrt(2 * n))
    else:
        return None


check = 2**4 * 3**4 * 5**4 * 7 * 11

while not is_triangle_number(check):
    check += 1

series_last_term = last_term(check)

while divisors(check) <= 500:
    check += (series_last_term + 1)
    series_last_term += 1
print(check)
