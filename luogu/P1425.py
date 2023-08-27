q = str(input()).split()
a=int(q[0])
b=int(q[1])
c=int(q[2])
d=int(q[3])

e = c - a
f = d - b
ans = e * 60 + f
print(ans//60 , ans%60)
