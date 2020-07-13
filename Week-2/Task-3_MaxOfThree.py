a = int(input())
b = int(input())
c = int(input())
maxEl = a
if a <= b and a <= c:
    if c <= b:
        maxEl = b
    else:
        maxEl = c
if b <= a and b <= c:
    if a <= c:
        maxEl = c
    else:
        maxEl = a
if c <= a and c <= b:
    if a <= b:
        maxEl = b
    else:
        maxEl = a
print(maxEl)
