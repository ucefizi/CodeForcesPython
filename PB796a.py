# Problem statement: http://codeforces.com/problemset/problem/796/A

x = [int(i) for i in input().split()]
n, m, k, = x[0], x[1]-1, x[2]
x = [int(i) for i in input().split()]
y = []
z = [0]*n
for i in range(n):
	y.append(abs(i-m))
for i in range(n):
	if x[i] != 0 and x[i] <= k:
		z[i] = y[i]
print(10*min(list(filter(lambda a: a != 0, z))))
