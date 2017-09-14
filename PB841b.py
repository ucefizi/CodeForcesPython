# Problem statement: http://www.codeforces.com/problemset/problem/841/B

N = int(input())
TAB = [int(i) for i in input().split()]
if sum(TAB) % 2:
	print('First')
else:
	X = list(filter(lambda x: x%2 == 1, TAB))
	if X:
		print('First')
	else:
		print('Second')
