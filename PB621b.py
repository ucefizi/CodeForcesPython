# Problem statement: http://www.codeforces.com/problemset/problem/621/B

tab = []
for i in range(int(input())):
	tab.append(input())
d = 0
i = 0
for i, v in enumerate(tab):
	j = i+1
	for j, w in enumerate(tab[i+1]):
		if int(w.split()[0]) - int(v.split()[0]) == int(w.split()[1]) - int(v.split()[1]):
			d += 1
print(d*2)
