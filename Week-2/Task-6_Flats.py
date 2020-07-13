x = int(input())
y = int(input())
flatsIn1 = y - x + 1
if x == 1:
    print('YES')
elif (x - 1) % flatsIn1 == 0:
    print('YES')
else:
    print('NO')
