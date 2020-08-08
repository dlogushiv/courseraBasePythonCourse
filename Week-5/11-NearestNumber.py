n = int(input())
a = list(map(int, input().split()))
x = int(input())
m = 2001
k = 0
for i in range(len(a)):
    m1 = abs(a[i] - x)
    if m1 < m:
        k = i
        m = m1
print(a[k])
