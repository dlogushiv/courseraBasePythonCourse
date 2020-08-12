n = int(input())
a = list(range(n - 1))
ideal = list(range(1, n + 1))
res = 0
for i in range(n - 1):
    a[i] = int(input())
for i in range(len(ideal)):
    k = 0
    for j in range(len(a)):
        if a[j] == ideal[i]:
            k += 1
    if k == 0:
        res = ideal[i]
print(res)
