a = list(map(int, input().split()))
minim = a[0]
x = 0
maksi = a[0]
y = 0
for i in range(len(a)):
    if a[i] < minim:
        minim = a[i]
        x = i
    if a[i] > maksi:
        maksi = a[i]
        y = i
(a[x], a[y]) = (a[y], a[x])
for i in range(len(a)):
    print(a[i], end=' ')
