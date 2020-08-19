a = list(map(int, input().split()))
k = 0
l = len(a)
i = 0
while i < l:
    if a[i - 1] == 0:
        k += 1
        a.pop(i - 1)
        i -= 1
        l -= 1
    i += 1
for i in range(k):
    a.append(0)
print(*a)
