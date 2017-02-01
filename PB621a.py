
n=int(input())
tab=[int(i) for i in input().split()]
tab.sort()
i=0
sum=0
while(i<n):
	sum+=tab[i]
	i+=1
som=sum
i=0
isEven=(sum%2==0)	
while(not(isEven)):
	sum=som-tab[i]
	i+=1
	isEven=(sum%2==0)

print(sum)