n = int(input())
tab = [int(i) for i in input().split()]
x = max(tab)
y = 0
for i in tab:
	y += x - i
print(y)