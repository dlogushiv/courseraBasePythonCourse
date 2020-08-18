def Intersection(a, b):
    res = []
    i = j = 0
    # variant with long run time
    # for i in a:
    #     for j in b:
    #         if i == j:
    #             res.append(i)
    #             continue

    # variant with good run time
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1

    return res


x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(*Intersection(x, y))
