def countSort(a):
    countList = [0] * (max(a) + 1)
    i = 0
    for el in a:
        countList[el] += 1
    for k in range(len(countList)):
        for j in range(countList[k]):
            a[i] = k
            i += 1
    return a


x = list(map(int, input().split()))
print(*countSort(x))
