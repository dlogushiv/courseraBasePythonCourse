l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
x1 = 0
y1 = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0
# 1
if l2 >= l1 <= l3:
    (otr1, x1, y1) = (1, l1, r1)
    if l2 <= l3:
        (otr2, x2, y2) = (2, l2, r2)
        (otr3, x3, y3) = (3, l3, r3)
    elif l3 <= l2:
        (otr2, x2, y2) = (3, l3, r3)
        (otr3, x3, y3) = (2, l2, r2)

# 2
if l1 > l2 <= l3:
    (otr1, x1, y1) = (2, l2, y2)
    if l1 <= l3:
        (otr2, x2, y2) = (1, l1, r1)
        (otr3, x3, y3) = (3, l3, r3)
    elif l3 < l1:
        (otr2, x2, y2) = (3, l3, r3)
        (otr3, x3, y3) = (1, l1, r1)
# 3
if l1 > l3 < l2:
    (otr1, x1, y1) = (3, l3, y3)
    if l1 <= l2:
        (otr2, x2, y2) = (1, l1, r1)
        (otr3, x3, y3) = (2, l2, r2)
    elif l2 < l1:
        (otr2, x2, y2) = (2, l2, r2)
        (otr3, x3, y3) = (1, l1, r1)

a = x2 - y1
b = x3 - y2
d1 = y1 - x1
d2 = y2 - x2
d3 = y3 - x3

# all crossed
if a <= 0 and b <= 0:
    print(0)
elif a <= 0 and b > 0:
    print(otr3)
elif a > 0 and b <= 0:
    print(otr1)

elif b <= d1:
    print(otr1)
elif b > d1 and a <= d3:
    print(otr3)
elif a > d3 and b > d1:
    print(-1)