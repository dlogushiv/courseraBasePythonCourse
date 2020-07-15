a, b, c = int(input()), int(input()), int(input())
while not a <= b <= c:
    if a > b:
        (a, b) = (b, a)
    if b > c:
        (b, c) = (c, b)
print(a, b, c)
