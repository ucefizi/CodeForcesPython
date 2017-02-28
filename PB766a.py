s1 = input()
s2 = input()
if s1 == s2: print(-1)
else:
	if len(s1) >= len(s2): print(len(s1))
	else: print(len(s2))