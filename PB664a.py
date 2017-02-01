# -*- coding: utf-8 -*-
def gcd(a,b):
	if a==0 : 
		return b
	elif b==0 :
		return a
	return(gcd(b%a,a))
x=[int(i) for i in input().split()]
if x[0]==x[1]: 
    print(x[0])
elif(x[0]+1==x[1]) :
    print(gcd(x[0],x[1]))
else :
    print(1)