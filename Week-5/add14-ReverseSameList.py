a = list(map(int, input().split()))
l = len(a)
if l % 2 == 1:
    l2 = (l - 1) // 2
else:
    l2 = l // 2
for i in range(l2):
    (a[i], a[l - 1 - i]) = (a[l - 1 - i], a[i])
print(*a)
