a = list(map(int, input().split()))
maks = a[0]
x = 0
for i in range(len(a)):
    if a[i] > maks:
        maks = a[i]
        x = i
print(maks, x)
