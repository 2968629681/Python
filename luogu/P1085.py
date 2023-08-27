a = []
b = []
flag = 0
smax=-1
ans = 0
for i in range(7):
    a.append(input().split(" "))
    b.append(int(a[i][0])+int(a[i][1]))
    if ((b[i] > 8) and b[i]>smax):
        if b[i]>smax:
            smax=b[i]
            ans=i+1
        else:
            ans=i+1
print(ans)
