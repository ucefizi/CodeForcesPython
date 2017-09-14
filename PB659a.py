# Problem statement: http://www.codeforces.com/problemset/problem/659/A

x = [int(i) for i in input().split()]
n, a, b = x[0], x[1], x[2]
if n == 0 or n == 1:
	print(n)
elif b == 0:
	print(a)
else:
	if b > 0:
		for i in range(b):
			if a == n:
				a = 0
				a += 1
			else:
				a += 1
		print(a)
	else:
		b = -b
		for i in range(b):
			if a == 1:
				a = n+1
				a -= 1
			else:
				a -= 1
		print(a)
