from math import sqrt, tan, radians

tab=[float(i) for i in input().split()]

a3=(tab[0]**3)*(sqrt(33))/48
a4=(tab[1]**3)*(sqrt(2))/6
a5=(tab[2]**3)*(5/24)*tan(radians(54))*sqrt(3-(tan(radians(54)))**2)

print(a3+a4+a5)

# Float problem???
# Unfinished