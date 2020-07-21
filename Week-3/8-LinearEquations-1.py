a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == 0 and d == 0:
    x = f / c
    y = e / b
elif d != 0:
    x = (e * d - b * f) / (a * d - b * c)
    y = (f - c * x) / d
else:
    x = f / c
    y = (e - a * x) / b
print(x, y)
