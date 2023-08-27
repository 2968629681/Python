l = [5,61,6,168,135,13,54,3,135,46]
da = len(l)
for i in range(1,da):
    for j in range(0,da-i):
        if l[j]>l[j+1]:
            temp = l[j+1]
            l[j+1] = l[j]
            l[j] = temp
print(l)
