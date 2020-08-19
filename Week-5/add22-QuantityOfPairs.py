a = list(map(int, input().split()))
quant = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            quant += 1
print(quant)
