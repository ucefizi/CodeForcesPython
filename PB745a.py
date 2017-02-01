st = input()
tab = []
for i in range(len(st)):
	tab.append(st)
	st = st[-1:]+st[:-1]
print(len(set(tab)))