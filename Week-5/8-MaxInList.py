a = list(map(int, input().split()))
max = a[0]
x = 0
for i in range(len(a)):
    if a[i] >= max:
        max = a[i]
        x = i
print(max, x)
