from math import gcd


def digit_cancelling_fractions():
    dp = 1
    np = 1

    c = 1
    while c <= 9:
        d = 1
        while d < c:
            n = 1
            while n < d:
                if ((n * 10 + c) * d) == ((c * 10 + d) * n):
                    np *= n
                    dp *= d
                n += 1
            d += 1
        c += 1
    return dp / gcd(np, dp)


print(digit_cancelling_fractions())
