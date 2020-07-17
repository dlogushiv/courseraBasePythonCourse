a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if (d == a and e == b) or (d == b and e == a):
    print('YES')
elif (d == a and e == c) or (d == c and e == a):
    print('YES')
elif (d == b and e == c) or (d == c and e == b):
    print('YES')
else:
    print('NO')
# a; b -> d=a & e=b | d=b & e=a
# a; c -> d=a & e=c | d=c & e=a
# b; c -> d=b & e=c | d=c & e=b
