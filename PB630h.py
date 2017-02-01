import math
import operator as op
import functools as fun
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = fun.reduce(op.mul, range(n, n-r, -1))
    denom = fun.reduce(op.mul, range(1, r+1))
    return numer//denom
n=int(input())
m=(ncr(n,5)*math.factorial(n))/n
print(m)