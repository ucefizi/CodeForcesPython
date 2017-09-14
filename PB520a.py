# Problem statement: http://www.codeforces.com/problemset/problem/520/A

n = input()
st = input()
strg = 'abcdefghijklmnopqrstuvwxyz'
d = 0
for char in strg:
	if char in st or char.upper() in st:
		d += 1
if d != 26:
	print("NO")
else:
	print("YES")
