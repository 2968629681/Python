while(1):
    flag = False
    great = input()
    for temp in great:
        if(temp<'0' or temp>'9'):
            print("请输入正确的格式")
            flag = True
            break
    if flag:
        continue
    great = eval(great)
    if great > 90:
        print("数字过大")
    elif great > 80:
        print("优秀")
    elif great > 70:
        print("良好")
    elif great > 60:
        pring("及格")
    elif great > 0:
        print("不及格")
    else:
        print("输入错误")
