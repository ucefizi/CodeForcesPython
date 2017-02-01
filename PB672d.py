# -*- coding: utf-8 -*-
x=[int(i) for i in input().split()]
n=x[0]
k=x[1]
tab=[int(i) for i in input().split()]
if min(tab)==max(tab): print("0")
else:
    i=0
    while i<k and max(tab)!=min(tab):
        mi=min(tab)
        ma=max(tab)
        tab[tab.index(mi)]+=1
        tab[tab.index(ma)]-=1
        i+=1
    print(max(tab)-min(tab))