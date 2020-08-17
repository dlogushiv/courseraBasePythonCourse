n=int(input())
town=list(map(int,input().split()))
mappedTowns=list(range(n))
m=int(input())
bu=list(map(int,input().split()))
mappedBU=list(range(m))
for i in range(len(town)):
    mappedTowns[i]=town[i], i
for i in range(len(bu)):
    mappedBU[i]=bu[i],i
mappedTowns.sort()
mappedBU.sort()
print(*mappedTowns)
print(*mappedBU)