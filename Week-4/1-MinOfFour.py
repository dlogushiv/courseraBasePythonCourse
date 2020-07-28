def min4(a, b, c, d):
    x = min(a, b)
    y = min(c, d)
    return min(x, y)


in1 = int(input())
in2 = int(input())
in3 = int(input())
in4 = int(input())
print(min4(in1, in2, in3, in4))
