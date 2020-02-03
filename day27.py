def horner_method(n):
    return (n * (n * (4 * n + 3) + 8) - 9) // 6


print(horner_method(1001))
