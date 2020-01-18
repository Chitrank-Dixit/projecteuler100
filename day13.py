def collatz_seqeunce(num):
    count = 0
    while num != 1:
        if num % 2 != 0:
            num = (3*num) + 1
        elif num % 2 == 0:
            num = num //2
        count += 1
    return count


max_count = 0
number = None
for i in range(1000000, 2, -1):
    count = collatz_seqeunce(i)
    if count > max_count:
        max_count = count
        number = i


print(max_count, number)
