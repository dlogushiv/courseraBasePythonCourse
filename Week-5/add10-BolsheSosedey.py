myList = list(map(int, input().split()))
k = 0
for i in range(1, len(myList) - 1):
    if myList[i - 1] < myList[i] > myList[i + 1]:
        k += 1
print(k)
