s = input()
subs = "f"
pos1 = s.find(subs)
pos2 = s[::-1].find(subs)
k = len(s) - pos2 - 1
if pos1 == -1:
    print("")
elif pos1 == k:
    print(pos1)
else:
    print(pos1, k)
