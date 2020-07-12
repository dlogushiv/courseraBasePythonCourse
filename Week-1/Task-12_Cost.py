costRub = int(input())
costKop = int(input())
quant = int(input())

cost = costRub * 100 + costKop
totalCost = cost * quant
print(totalCost // 100, totalCost % 100)
