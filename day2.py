check = 0
num = 600851475143

prime_factor = 2


while num >= (prime_factor * prime_factor):
    if num % prime_factor == 0:
        num = num / prime_factor
    else:
        prime_factor += 1


print("largest prime factor is: ", num)
