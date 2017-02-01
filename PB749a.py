n = int(input())
if n%2 == 0 and n != 2:
	print(n//2)
	print(' '.join(['2' for i in range(n//2)]))
elif n%2 != 0:
	print((n-1)//2)
	print(' '.join(['2' for i in range((n-3)//2)]), 3)
else:
	print(1)
	print(2)