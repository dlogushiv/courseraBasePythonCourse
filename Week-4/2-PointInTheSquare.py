def isPointInSquare(fx, fy):
    return (-1 <= fx <= 1) and (-1 <= fy <= 1)


x = float(input())
y = float(input())

if isPointInSquare(x, y):
    print('YES')
else:
    print('NO')
