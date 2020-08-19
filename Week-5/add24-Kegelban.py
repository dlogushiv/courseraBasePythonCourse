inData = list(map(int, input().split()))
n = inData[0]
k = inData[1]
res = []
for i in range(n):
    res.append('I')
for j in range(k):
    brknKeg = list(map(int, input().split()))
    for keg in range(brknKeg[0] - 1, brknKeg[1]):
        res[keg] = '.'
print(*res, sep='')
