# Problem statement: http://www.codeforces.com/problemset/problem/765/A

n = int(input())
home = input()
src = []
dest = []
for i in range(n):
	x = input().split('->')
	src.append(x[0])
	dest.append(x[1])
cs = src.count(home)
cd = dest.count(home)
if cs > cd:
	print('contest')
else:
	print('home')
