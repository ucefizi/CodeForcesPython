# Problem statement: http://www.codeforces.com/problemset/problem/749/B

A = [float(i) for i in input().split()]
B = [float(i) for i in input().split()]
C = [float(i) for i in input().split()]
cAB = [(A[0]+B[0])/2, (A[1]+B[1])/2]
cAC = [(A[0]+C[0])/2, (A[1]+C[1])/2]
cBC = [(C[0]+B[0])/2, (C[1]+B[1])/2]
p1 = [2*cAB[0]-C[0], 2*cAB[1]-C[1]]
p2 = [2*cAC[0]-B[0], 2*cAC[1]-B[1]]
p3 = [2*cBC[0]-A[0], 2*cBC[1]-A[1]]
print(3)
print(int(p1[0]), int(p1[1]))
print(int(p2[0]), int(p2[1]))
print(int(p3[0]), int(p3[1]))
