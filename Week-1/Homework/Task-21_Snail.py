H = int(input())
A = int(input())
B = int(input())
inDay = A - B
days = (H - B - 1) // inDay + 1
print(days)
