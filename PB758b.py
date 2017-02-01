tab = list(input())
if '!' not in tab: print(0, 0, 0, 0)
else:
	dic = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
	for i in range(len(tab)):
		if tab[i] == '!':
			for j in range(len(tab)):
				if i%4 == j%4 and tab[j] != '!':
					dic[tab[j]] += 1
					break
	print(dic['R'], dic['B'], dic['Y'], dic['G'])