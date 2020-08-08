n = int(input())
r1 = '+___ '
r2 = ''
r3 = '|__\ '
r4 = '|    '
r = [r1, r2, r3, r4]
r[0] = r1 * n
r[2] = r3 * n
r[3] = r4 * n

for i in range(1, n + 1):
    r[1] += '|' + str(i) + ' / '

for i in range(len(r)):
    print(r[i])
