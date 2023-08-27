k=int(input())
sum = 0
ant = 1
sum = ant
res = 0
while(k>0):
    res +=ant
    sum -=1
    if sum == 0:
        sum = ant+1
        ant +=1
    k-=1
print(res)
    
