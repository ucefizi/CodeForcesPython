# Problem statement: http://www.codeforces.com/problemset/problem/672/A

n = int(input())
if n < 10:
	print(n)
else:
	strg = ""
	for i in range(n+1):
		strg += str(i)
	print(strg[n])
