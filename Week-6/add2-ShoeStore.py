size = int(input())
stock = sorted(list(map(int, input().split())))
res = 0
prevShoe = 0
for shoe in stock:
    if shoe >= size and prevShoe == 0:
        res += 1
        prevShoe = shoe
    elif prevShoe != 0 and shoe - prevShoe >= 3:
        res += 1
        prevShoe = shoe
print(res)
