def fact(a):
    if a > 1:
        return a * fact(a - 1)
    else:
        return 1


n = int(input())
res = 0
for i in range(n):
    res += fact(i + 1)
print(res)
