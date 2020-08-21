n = int(input())
myList = []
for i in range(n):
    myList.append(tuple(map(str, input().split())))
myList.sort(key=lambda x: int(x[1]), reverse=True)
for el in myList:
    print(el[0])
