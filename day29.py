def get_digits(n):
    digit_list = []
    while n != 0:
        digit_list.append((n%10) ** 5)
        n //= 10
    return sum(digit_list)


def sum_of_fifth_powers(n):
    num_sum = 0
    for i in range(2, n):
        if i == get_digits(i):
            num_sum += i
    return num_sum


print(sum_of_fifth_powers(10000000))
