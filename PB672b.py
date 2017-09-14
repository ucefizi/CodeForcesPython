# Problem statement: http://www.codeforces.com/problemset/problem/672/B

n = int(input())
strg = input()
x = 0
if n > 26:
	print(-1)
else:
	while strg:
		c = strg[0]
		strg = strg[1:]
		if c in strg:
			x += 1
	print(x)
