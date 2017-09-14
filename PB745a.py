# Problem statement: http://www.codeforces.com/problemset/problem/745/A

st = input()
tab = []
for i in range(len(st)):
	tab.append(st)
	st = st[-1:] + st[:-1]
print(len(set(tab)))
