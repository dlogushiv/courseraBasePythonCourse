a = list(map(int, input().split()))
m = 0
for i in a:
    if i % 2 == 1:
        if m == 0 or i < m:
            m = i
print(m)
