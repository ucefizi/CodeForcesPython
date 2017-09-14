# Problem statement: http://www.codeforces.com/problemset/problem/660/B

tab = [int(i) for i in input().split()]
n, m = tab[0], tab[1]
x = ""
if m == 4*n:
	for i in range(n):
		x += str(2*n+1+2*i) + " " + str(2*i+1) + " " + str(2*n+2+2*i) + " " + str(2*i+2) + " "
else:
	for i in range(n):
		if 2*n + 2*i + 1 <= m:
			x += str(2*n+2*i+1) + " "
		if 2*i + 1 <= m:
			x += str(2*i+1) + " "
		if 2*n + 2*i + 2 <= m:
			x += str(2*n+2*i+2) + " "
		if 2*i + 2 <= m:
			x += str(2*i+2) + " "
x = x[:-1]
print(x)
