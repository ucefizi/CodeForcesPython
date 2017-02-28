st = (list(input()))
s = sorted(set(st), key=st.index)
n = len(s)
x = 'YES'
for i in range(n):
	if ord(s[i])-97 != i:
		x = 'NO'
print(x)