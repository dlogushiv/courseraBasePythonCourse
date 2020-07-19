k = int(input())
s = 0
i = 0
while s <= k:
    i += 1
    s = i ** 2
    if s <= k:
        print(s, end=' ')
