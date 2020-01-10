def reverse(number):
    rev = 0
    while number > 0:
        remainder = number % 10
        rev = (rev * 10) + remainder
        number //= 10
    return rev


max = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        p1 = reverse(product)
        if (p1 == product) and (p1 > max):
            max = p1
print(max)


