import re
n = int(input())
p1 = r'^R([0-9]+)C([0-9]+)$'
p2 = r'^([A-Z]+)([0-9]+)$'
for i in range(n):
	s = input()
	if re.match(p1, s):
		s1 = int(re.search(r'R([0-9]+)', s).group(1))
		s2 = int(re.search(r'C([0-9]+)', s).group(1))
		print(s1, s2)
	elif re.match(p2, s):
		s1 = re.search(r'([A-Z]+)', s).group(1)
		x1 = 0
		for i in range(len(s1)):
		    x1 += (ord(s1[-i])-64)*26**(i)
		s2 = int(re.search(r'([0-9]+)', s).group(1))
		print(x1, s2)

		# *** Unfinished...