from itertools import compress


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p) <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return list(compress(range(len(prime)), prime))


dictio = sieve_of_eratosthenes(2000000)
print(sum(dictio))
