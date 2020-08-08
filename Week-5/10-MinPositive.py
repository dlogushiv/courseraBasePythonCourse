a = list(map(int, input().split()))
m = 1000
for i in range(len(a)):
    if a[i] > 0 and a[i] < m:
        m = a[i]
print(m)
