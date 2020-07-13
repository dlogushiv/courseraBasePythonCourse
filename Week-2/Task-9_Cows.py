x = int(input())
if 5 <= x <= 20 or x % 10 == 5 or x % 10 == 6 or x % 10 == 7 \
        or x % 10 == 8 or x % 10 == 9 or x % 10 == 0:
    print(x, 'korov')
elif x == 1 or (x % 10 == 1 and x != 11):
    print(x, 'korova')
else:
    print(x, 'korovy')
