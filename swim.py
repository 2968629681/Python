a = eval(input())
ant = 0;
sum = 2;
while(a>0):
    a-=sum
    sum *= 0.98
    ant+=1
print(ant)
