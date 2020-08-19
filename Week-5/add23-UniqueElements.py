a = list(map(int, input().split()))
l = len(a)
i = 0
while i < l:
    j = i + 1
    fl = False
    while j < l:
        if a[i] == a[j]:
            a.pop(j)
            l -= 1
            j -= 1
            fl = True
        j += 1
    if fl:
        a.pop(i)
        l -= 1
        i -= 1
    i += 1
print(*a)
