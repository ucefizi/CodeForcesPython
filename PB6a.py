# Problem statement: http://www.codeforces.com/problemset/problem/6/A

x = [int(i) for i in input().split()]
x.sort()
if x[3] < x[2]+x[1] or x[3] < x[2]+x[0] or x[3] < x[1]+x[0] or x[2] < x[1]+x[0]:
	print("TRIANGLE")
elif x[3] == x[2]+x[1] or x[3] == x[2]+x[0] or x[3] == x[1]+x[0] or x[2] == x[1]+x[0]:
	print("SEGMENT")
else:
	print("IMPOSSIBLE")
