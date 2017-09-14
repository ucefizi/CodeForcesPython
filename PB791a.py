# Problem statement: http://codeforces.com/problemset/problem/791/A

from math import ceil, floor, log
tb = [float(i) for i in input().split()]
x = log(tb[1]/tb[0], 3/2)
if floor(x) == ceil(x):
	print(ceil(x)+1)
else:
	print(ceil(x))
