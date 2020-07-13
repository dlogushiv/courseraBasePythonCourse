a = int(input())
b = int(input())
k = int(input())
if a * b > k and (k % a == 0 or k % b == 0):
    print('YES')
else:
    print('NO')
