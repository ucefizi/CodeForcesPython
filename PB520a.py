input("")
str=input("")
strg=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
d=0
for char in strg :
	if(char in str or char.upper() in str):
		d+=1

if(d!=26):
	print("NO")
else :
	print("YES")