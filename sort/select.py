l = [5,61,6,168,135,13,54,3,135,46]
len = len(l)
for i in range(len):
    for j in range(i+1,len):
        if l[i]>l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l)
