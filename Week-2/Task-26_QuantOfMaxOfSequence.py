a = int(input())
m = a
q = 0
while a != 0:
    if a > m:
        m = a
        q = 0
    if a == m:
        q += 1
    a = int(input())
print(q)
