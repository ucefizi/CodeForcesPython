# -*- coding: utf-8 -*-
x=[int(i) for i in input().split()]
if x[2]==0 and x[1]==x[0]: print("YES")
elif x[2]==0 and x[1]!=x[0]: print("NO")
elif (x[2]>0 and x[1]<x[0]) or (x[2]<0 and x[1]>x[0]): print("NO")
elif x[1]%x[2]==x[0]: print("YES")
else: print("NO")