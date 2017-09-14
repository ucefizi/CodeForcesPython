# Problem statement: http://www.codeforces.com/problemset/problem/841/A

TAB = [int(i) for i in input().split()]
S = list(input())
B = set(S)
C = [S.count(i) for i in S]
if max(C) <= TAB[1]:
	print('YES')
else:
	print('NO')
