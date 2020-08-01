def isPrime(n):
    i = 2
    if n == 2:
        return True
    while n % i != 0:
        if i ** 2 >= n:
            return True
        i += 1
    return False


x = int(input())
if isPrime(x):
    print('YES')
else:
    print('NO')
