rank = list(map(int, input().split()))
p = int(input())
for i in range(len(rank) - 1, -1, -1):
    if rank[i] >= p:
        print(i + 1 + 1)
        break
    elif i == 0:
        print(i + 1)
