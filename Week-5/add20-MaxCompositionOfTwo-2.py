a = list(map(int, input().split()))
p = n = a[:]
maxP1 = max(p)
p.pop(p.index(maxP1))
maxP2 = max(p)
minN1 = min(n)
n.pop(n.index(minN1))
minN2 = min(n)

if maxP1 * maxP2 > minN1 * minN2:
    print(maxP2, maxP1)
else:
    print(minN1, minN2)
