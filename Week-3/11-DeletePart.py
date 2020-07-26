s = input()
subs = "h"
pos1 = s.find(subs)
pos2 = s.rfind(subs)
s2 = s[pos1:pos2+1]
print(s.replace(s2, ""))
