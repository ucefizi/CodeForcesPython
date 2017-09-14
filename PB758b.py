# Problem statement: http://www.codeforces.com/problemset/problem/758/B

tab = list(input())
if '!' not in tab:
	print(0, 0, 0, 0)
else:
	dic = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
	for i, v in enumerate(tab):
		if v == '!':
			for j, w in enumerate(tab):
				if i%4 == j%4 and w != '!':
					dic[w] += 1
					break
	print(dic['R'], dic['B'], dic['Y'], dic['G'])
