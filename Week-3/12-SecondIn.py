s = input()
subs = "f"
pos1 = s.find(subs)
pos2 = s.find(subs, pos1 + 1)
if pos1 == -1:
    print("-2")
elif pos2 == -1:
    print("-1")
else:
    print(pos2)
