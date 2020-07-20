x = int(input())  # km in first day
y = int(input())  # km after last day
i = 1
s = x
while s < y:
    s = s + s * 0.1
    i += 1
print(i)
