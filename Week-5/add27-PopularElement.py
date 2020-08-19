a = list(map(int, input().split()))
m = mmax = a[0]
k = kmax = 0
for i in a:
    m = i
    for j in a:
        if i == j:
            k += 1
    if k > kmax:
        kmax = k
        mmax = m
    k = 0
print(mmax)
