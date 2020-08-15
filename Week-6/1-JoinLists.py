def merge(x, y):
    z = x + y
    # first variant works but not good
    # flag = False
    # while not flag:
    #     flag = True
    #     for i in range(len(z) - 1):
    #         if z[i] > z[i + 1]:
    #             flag = False
    #             (z[i], z[i + 1]) = (z[i + 1], z[i])
    # second variant
    i = j = 0
    for k in range(len(z)):
        if i > len(x) - 1:
            z[k] = y[j]
            j += 1
        elif j > len(y) - 1:
            z[k] = x[i]
            i += 1
        elif x[i] < y[j]:
            z[k] = x[i]
            i += 1
        else:
            z[k] = y[j]
            j += 1
    return z


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = merge(a, b)
print(*c)
