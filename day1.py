f1 = 0
f2 = 1
f3 = 0
total = 0
number = 36  # 36 would come up with f3 as 3524578, but 37 would have f3 > 4000000
for i in range(1, number+1):
    if f3 % 2 == 0:
        total = total + f3
    f1 = f2
    f2 = f3
    f3 = f1 + f2

print(total)
