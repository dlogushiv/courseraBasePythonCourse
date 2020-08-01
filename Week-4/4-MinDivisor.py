def min_divisor(n):
    i = 2
    # if n == 1 or n == 2 or n == 3:
    #     return n
    while n % i != 0:
        i += 1
        if i ** 2 > n:
            return n
    return i


x = int(input())
print(min_divisor(x))
