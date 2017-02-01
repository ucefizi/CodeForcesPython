n=int(input())
tab=[int(i) for i in input().split()]
tab.sort()
x=tab.pop()
print(x-sum(tab)+1)