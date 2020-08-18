n = int(input())
town = list(map(int, input().split()))
sT = list(range(n))
m = int(input())
bu = list(map(int, input().split()))
sB = list(range(m))
# создаем список из кортежей (город, индекс в начальном списке)
for i in range(len(town)):
    sT[i] = town[i], i
# создаем список из кортежей (бу, индекс в начальном списке)
for i in range(len(bu)):
    sB[i] = bu[i], i + 1
# сортируем полученные списки из кортежей просто по первому значению кортежа
sT.sort()
sB.sort()
i = 0
j = 0
res = list(range(n))
# если бу одно, то для каждого города оно будет ближайшим
if m == 1:
    for i in range(n):
        res[i] = sB[0][1]
while i < n and j < m - 1:
    if abs(sT[i][0] - sB[j][0]) <= abs(sT[i][0] - sB[j + 1][0]):
        res[sT[i][1]] = sB[j][1]
        i += 1
    else:
        j += 1
        # если дошли до последнего бу, то оно будет ближайшим для всех остальных городов
        if j == m - 1:
            while i < n:
                res[sT[i][1]] = sB[j][1]
                i += 1
        # иначе, проверяем текущий город со следующим бу
        elif abs(sT[i][0] - sB[j][0]) <= abs(sT[i][0] - sB[j + 1][0]):
            res[sT[i][1]] = sB[j][1]
            i += 1

print(*res)
