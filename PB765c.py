# Problem statement: http://www.codeforces.com/problemset/problem/765/C

tab = [int(i) for i in input().split()]
sa = int(tab[1]/tab[0])
sb = int(tab[2]/tab[0])
if (tab[1]%tab[0] != 0 and sb == 0) or (tab[2]%tab[0] != 0 and sa == 0) or (sa == 0 and sb == 0):
	print(-1)
else:
	print(sa + sb)
