# Problem statement: http://www.codeforces.com/problemset/problem/621/A

n = int(input())
tab = [int(i) for i in input().split()]
tab.sort()
i = 0
su = 0
while i < n:
	su += tab[i]
	i += 1
som = su
i = 0
isEven = su%2 == 0
while not isEven:
	su = som - tab[i]
	i += 1
	isEven = su%2 == 0
print(su)
