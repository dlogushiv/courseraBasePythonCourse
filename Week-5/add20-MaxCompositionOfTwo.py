a = list(map(int, input().split()))
maxP1 = maxP2 = None
minN1 = minN2 = None
for el in a:
    if el >= 0:
        if maxP1 is None:
            maxP1 = el
        elif el >= maxP1:
            maxP2 = maxP1
            maxP1 = el
    else:
        if minN2 is None:
            minN2 = el
        elif el <= minN2 and minN1 is None:
            minN1 = el
        else:
            minN1 = minN2
            minN2 = el

if minN1 is None or minN2 is None or maxP1 * maxP2 > minN1 * minN2:
    print(maxP2, maxP1)
elif maxP1 is None or maxP2 is None or maxP1 * maxP2 < minN1 * minN2:
    print(minN1, minN2)
