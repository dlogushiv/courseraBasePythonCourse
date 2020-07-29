def isPointInRhombus(fx, fy):
    return (-1 <= x + y <= 1) and (-1 <= x - y <= 1)


x = float(input())
y = float(input())

if isPointInRhombus(x, y):
    print('YES')
else:
    print('NO')
