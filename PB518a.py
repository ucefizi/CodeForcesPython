def nextC(ch) :
	if ch == 'z' : return 'a'
	else :
		return chr(ord(ch)+1)
def nextS(st) :
	tab = [i for i in st]
	i = len(tab)-1
	while tab[i] == 'z' :
		tab[i] = nextC(tab[i])
		i -= 1
	tab[i] = nextC(tab[i])
	return ''.join(tab)
s = input()
t = input()
st = nextS(s)
if s == st or t == st or s == t : print("No such string")
else : print(st)