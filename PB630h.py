# Problem statement: http://www.codeforces.com/problemset/problem/630/H

from math import factorial
from operator import mul
from functools import reduce

def ncr(n, r):
	r = min(r, n-r)
	if r == 0:
		return 1
	numer = reduce(mul, range(n, n-r, -1))
	denom = reduce(mul, range(1, r+1))
	return numer//denom

n = int(input())
print((ncr(n, 5)*factorial(n))/n)
