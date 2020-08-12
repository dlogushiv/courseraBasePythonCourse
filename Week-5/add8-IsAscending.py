def IsAscending(a):
    i = 0
    while i != len(a) - 1:
        if a[i + 1] <= a[i]:
            return False
        i += 1
    return True


myList = list(map(int, input().split()))
if IsAscending(myList):
    print('YES')
else:
    print('NO')
