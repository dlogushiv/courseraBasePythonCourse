def summa(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return summa(a + 1, b - 1)


x = int(input())
y = int(input())
print(summa(x, y))
