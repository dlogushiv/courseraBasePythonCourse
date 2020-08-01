def gsd(a, b):
    if b % a == 0:
        return a
    else:
        return gsd(b, a % b)


x = int(input())
y = int(input())
print(x // gsd(x, y), y // gsd(x, y))
