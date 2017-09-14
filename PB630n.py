# Problem statement: http://www.codeforces.com/problemset/problem/630/N

from math import sqrt
tab = [int(i) for i in input().split()]
de = pow(tab[1], 2) - 4*tab[0]*tab[2]
x1 = (-tab[1] - sqrt(de))/(2*tab[0])
x2 = (-tab[1] + sqrt(de))/(2*tab[0])
print("{:10.10f}".format(max(x1, x2)))
print("{:10.10f}".format(min(x1, x2)))
