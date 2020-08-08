a = list(map(int, input().split()))
if len(a) % 2 == 0:
    n = len(a)
else:
    n = len(a) - 1
for i in range(0, n, 2):
    (a[i], a[i + 1]) = (a[i + 1], a[i])
for i in range(len(a)):
    print(a[i], end=' ')
