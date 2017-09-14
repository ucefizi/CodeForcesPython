# Problem statement: http://www.codeforces.com/problemset/problem/1/A

from math import ceil
tab = [int(i) for i in input().split()]
print(ceil(tab[0]/tab[2])*ceil(tab[1]/tab[2]))
