p = int(input())
x = int(input())
y = int(input())
xy = x + y / 100
yp = xy + xy * p / 100
print(int(yp // 1), int(round(((yp % 1) * 100), 2)))
