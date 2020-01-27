from array import array


def find_abundant(number):
    import math
    sum_factor = 1
    value = math.ceil(math.sqrt(number))
    if number == 1:
        return False
    for i in range(2, value):
        if number % i == 0:
            sum_factor += (i+(number//i))
    if value**2 == number:
        sum_factor += value
    if sum_factor > number:
        return True
    else:
        return False


numbers = [0]*28123
abundant_numbers = array("i", [])
for abundant in range(1, 28124):
    if find_abundant(abundant):
        abundant_numbers.append(abundant)

for x in abundant_numbers:
    for y in abundant_numbers[0:abundant_numbers.index(x)+1]:
        z = x+y
        if z < 28124 and numbers[z-1] == 0:
            numbers[z-1] = z


_sum = 0
for vary in range(1, len(numbers)+1):
    if numbers[vary-1] == 0:
        _sum += vary
print(_sum)
