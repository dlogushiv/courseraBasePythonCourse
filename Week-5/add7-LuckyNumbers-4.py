a = int(input())
b = int(input())
for i in range(a, b + 1):
    c = tuple(str(i))
    if c[0] == c[-1] and c[1] == c[-2]:
        print(i)
