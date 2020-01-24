import math


def factorial_digit_sum(n):
    fact = math.factorial(n)
    digit_sum = 0
    while fact !=0:
        digit_sum += fact % 10
        fact = fact // 10
    return digit_sum


print(factorial_digit_sum(100))
