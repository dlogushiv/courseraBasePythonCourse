def summ(k):
    if k != 0:
        n = int(input())
        return k + summ(n)
    else:
        return k


x = int(input())
print(summ(x))
