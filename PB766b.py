# Problem statement: http://www.codeforces.com/problemset/problem/766/B

def func(tab, n):
	tab.sort(reverse=True)
	for i in range(n-2):
		for j in range(i+1, n-1):
			if tab[i] < tab[j] + tab[j+1]:
				return 'YES'
	return 'NO'

n = int(input())
tab = [int(i) for i in input().split()]
print(func(tab, n))
