a = list(map(int, input().split()))
x = 0
y = 0
for i in range(len(a) - 2, -1, -1):
    if (a[i] > 0 and a[i + 1] > 0) or (a[i] < 0 and a[i + 1] < 0):
        y = a[i + 1]
        x = a[i]
# for i in range(len(a) - 1):
#     if (a[i] > 0 and a[i + 1] > 0) or (a[i] < 0 and a[i + 1] < 0):
#         y = a[i + 1]
#         x = a[i]
#         break
if x != 0 and y != 0:
    print(x, y)
