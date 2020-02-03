def distinct_powers(n):
    nums = []
    for i in range(2, n+1):
        for j in range(2, n+1):
            nums.append(i**j)
    print(nums)
    return len(set(nums))


print(distinct_powers(100))
