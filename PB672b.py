# -*- coding: utf-8 -*-

n=int(input())
strg=input()
x=0
if n>26: print(str(-1))
else:
    while len(strg)>0:
        c=strg[0]
        strg=strg[1:]
        if c in strg: x+=1
    print(x)