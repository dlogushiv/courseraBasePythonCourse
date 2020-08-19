a = list(map(int, input().split()))
if len(a) == 3:
    print(*a)
else:
    p = n = a[:]
    maxP1 = max(p)
    p.pop(p.index(maxP1))
    maxP2 = max(p)
    p.pop(p.index(maxP2))
    maxP3 = max(p)

    minN1 = min(n)
    n.pop(n.index(minN1))
    minN2 = min(n)

    if maxP1 * maxP2 * maxP3 > minN1 * minN2 * maxP1:
        print(maxP3, maxP2, maxP1)
    else:
        print(minN1, minN2, maxP1)
