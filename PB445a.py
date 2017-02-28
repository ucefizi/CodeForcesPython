tab = [int(i) for i in input().split()]
for i in range(tab[0]):
	s = list(input())
	for j in range(tab[1]):
		if s[j] == '.':
			if (i+j)%2 == 1: s[j] = 'W'
			else: s[j] = 'B'
	print(''.join(s))