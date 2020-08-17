freeSpace, users = list(map(int, input().split()))
spaceByUser = list(range(users))
for i in range(len(spaceByUser)):
    spaceByUser[i] = int(input())
space = 0
counter = 0
spaceByUser.sort()
for i in range(len(spaceByUser)):
    if freeSpace > space + spaceByUser[i]:
        space += spaceByUser[i]
        counter += 1
print(counter)
