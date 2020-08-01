def degree(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        return degree(a ** 2, n / 2)
    else:
        return a * degree(a, n - 1)


x = float(input())
y = int(input())
print(degree(x, y))
