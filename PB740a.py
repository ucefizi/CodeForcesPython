# Problem statement: http://www.codeforces.com/problemset/problem/740/A

tab = [int(i) for i in input().split()]
if tab[0]%4 == 0:
	print(0)
elif tab[0]%4 == 1:
	print(min(tab[3], 3*tab[1], tab[1]+tab[2]))
elif tab[0]%4 == 2:
	print(min(tab[2], 2*tab[1], 2*tab[3]))
else:
	print(min(tab[1], tab[2]+tab[3], 3*tab[3]))
