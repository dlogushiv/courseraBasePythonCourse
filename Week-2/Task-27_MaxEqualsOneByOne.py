a = int(input())
q1 = 1
q2 = 1
qm = 0
while a != 0:
    k = a
    a = int(input())
    if k == a:
        q1 += 1
    else:
        q2 = q1
        q1 = 1
    if q1 >= qm:
        qm = q1
print(qm)
