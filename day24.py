def fibonacci_nums(num):
    i = 0
    f1 = 0
    f2 = 1
    f3 = 0
    while i < (num):
        f1 = f2
        f2 = f3
        f3 = f1 + f2
        if (f3 // (10 ** 999)) != 0:
            break
        i += 1
    return i+1

print(fibonacci_nums(1000000))
