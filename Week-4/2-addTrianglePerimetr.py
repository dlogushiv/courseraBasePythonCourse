def dist(x1, y1, x2, y2):
    dx = abs(max(x1, x2) - min(x1, x2))
    dy = abs(max(y1, y2) - min(y1, y2))
    return (dx ** 2 + dy ** 2) ** 0.5


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

print(dist(x1, y1, x2, y2) + dist(x1, y1, x3, y3) + dist(x2, y2, x3, y3))
