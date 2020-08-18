myList = list(map(int, input().split()))
k = int(input())
for i in range(k, len(myList) - 1):
    myList[i] = myList[i + 1]
myList.pop(-1)
print(*myList)
