tab=[int(i) for i in input().split()]
n=tab[0]
m=tab[1]
x=""
if m==4*n :
	for i in range(n) :
		x=x+str(2*n+1+2*i)+" "+str(2*i+1)+" "+str(2*n+2+2*i)+" "+str(2*i+2)+" "
else :
	for i in range(n) :
		if 2*n+2*i+1<=m :
			x=x+str(2*n+2*i+1)+" "
		if 2*i+1<=m :
			x=x+str(2*i+1)+" "
		if 2*n+2*i+2<=m :
			x=x+str(2*n+2*i+2)+" "
		if 2*i+2<=m :
			x=x+str(2*i+2)+" "

x=x[:-1]		
		
print(x)