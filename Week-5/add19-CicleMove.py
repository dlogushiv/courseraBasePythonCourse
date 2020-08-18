a = list(map(int, input().split()))
tmp = a[len(a) - 1]
for i in range(len(a) - 1, -1, -1):
    a[i] = a[i - 1]
a[0] = tmp
print(*a)
