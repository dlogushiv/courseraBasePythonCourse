myList = list(map(int, input().split()))
data = list(map(int, input().split()))
k = data[0]
c = data[1]
myList.append(0)
for i in range(len(myList) - 1, k, -1):
    myList[i] = myList[i - 1]
myList[k] = c
print(*myList)
