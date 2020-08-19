fileIn = open('5-input.txt', 'r', encoding='utf8')
s9 = 0
c9 = 0
s10 = 0
c10 = 0
s11 = 0
c11 = 0
for line in fileIn.readlines():
    st = tuple(line.split())
    if int(st[2]) == 9:
        s9 += int(st[3])
        c9 += 1
    if int(st[2]) == 10:
        s10 += int(st[3])
        c10 += 1
    if int(st[2]) == 11:
        s11 += int(st[3])
        c11 += 1
fileIn.close()
print(s9 / c9, s10 / c10, s11 / c11)
