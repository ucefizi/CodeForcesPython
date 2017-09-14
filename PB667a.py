# Problem statement: http://www.codeforces.com/problemset/problem/667/A

from math import pi
tab = [float(i) for i in input().split()]
d, h, v, e = tab[0], tab[1], tab[2], tab[3]
he = 4*v/(pi*d**2)
if e >= he:
	print("NO")
else:
	t = h/(he-e)
	print("YES")
	print(t)
