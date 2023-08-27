for i in range(10000):
    flag = False
    if 0 <= i <=9:
        flag=True
    elif 10 <= i <= 99:
        a = i % 10
        b = ( i // 10 ) % 10
        if a == b:
            flag=True
    elif 100 <= i <= 999:
        a = i % 10
        b = ( i // 10 ) % 10
        c = ( i // 100) % 10
        if a == c:
            flag=True
    elif 1000 <= i <= 9999:
        a = i % 10
        b = ( i // 10 ) % 10
        c = ( i // 100) % 10
        d = ( i // 1000) % 10
        if a == d and b == c:
            flag=True
    if flag:
        book = True
        for j in range(2,i-1):
            if i % j == 0:
                book = False
                break
        if book:
            print(i)
        
