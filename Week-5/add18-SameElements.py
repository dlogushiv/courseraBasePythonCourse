a = list(map(int, input().split()))
res = 1
for i in range(1, len(a)):
    if a[i - 1] != a[i]:
        res += 1
print(res)
