def pythagoream_triplet(n):
    for i in range(1, int(n / 3) + 1):
        for j in range(i + 1, int(n / 2) + 1):
            k = n - i - j
            if (i * i + j * j == k * k) and (i + j + k == 1000):
                return i*j*k


print(pythagoream_triplet(1000))
