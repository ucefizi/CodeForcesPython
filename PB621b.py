n=int(input())
tab=[""]*n
i=0
while(i<n):
	tab[i]=input()
	i+=1

d=0
i=0
while(i<n):
	j=i+1
	while(j<n):
		if(int(tab[j].split()[0])-int(tab[i].split()[0]) == int(tab[j].split()[1])-int(tab[i].split()[1])) :
			d+=1
		j+=1
	i+=1
print(d*2)