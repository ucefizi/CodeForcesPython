# Problem statement: http://www.codeforces.com/problemset/problem/675/A

x = [int(i) for i in input().split()]
if (x[2] == 0 and x[1] == x[0]) or (x[1]%x[2] == x[0]):
	print("YES")
else:
	print("NO")
