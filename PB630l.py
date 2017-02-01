m=[int(i) for i in input()]
m[1], m[2] = m[2], m[1]
m[2], m[4] = m[4], m[2]
print(str(pow(m[0]*10000+m[1]*1000+m[2]*100+m[3]*10+m[4], 5, 100000)).zfill(5))