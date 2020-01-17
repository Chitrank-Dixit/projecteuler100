filename = 'p12.txt'
with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)

int_array = []

for i in array:
    int_array.append(int(i))

array_sum = sum(int_array)
print(str(array_sum)[:10])
