a = list(map(int, input().split()))
l = len(a)
b = list(range(l))
for i in range(l):
    b[l - 1 - i] = a[i]
print(*b)
