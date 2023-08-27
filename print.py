flag = True
for temp in range(100):
    if flag:
        print(" ",end="")
        flag = False
    else:
        print("*",end="")
        flag = True
