#   引入随机数
import random

# users_info = [
#     # 0:用户名 1:密码 2:VIP等级 3:姓名 4:电话 5:地址 6:邮编 7:余额 8:生日 9:个性签名 10.购物车 11.订单管理
#     ['123', '123', 'diamond', 'lining', '131131313131', '山西省晋中市', '044000', '0', '2002-2-31',
#     '谦谦君子，温润如玉', [], []]
# ]

users_info = {
    "123": {"name": "123", "password": "123", "VIP": "diamond", "real_name": "lining", "address": "山西省晋中市",
            "birthday": "20011112", "phone": "156165156", "postal": "030053",
            "signature": "aaaaaaaa", "money": "0", "cart": [], "order": []}
}

admin_info = [
    # 0:用户名 1:密码
    ['guochengyu', '123456']
]

book_info = [
    # 1. 根据书名查  2. 根据ISBN查  3. 根据作者查    4. 根据类别查    5. 根据出版社查   6. 根据关键字查   7. 根据出版时间查  8.价格
    ['书名', 'ISBN', '作者', '类别', '出版社', '关键字', '出版时间', '10'],
    ['123', '12221', '作者', '类别', '出版社', '关键字', '出版时间', '20'],
    ['456', '0222002', '作者', '类别', '出版社', '关键字', '出版时间', '30']
]


def modify_user_name():
    """
    Modify the user's username by entering it
    :return: None
    """

    while True:
        change_user = input("请输入你要修改谁的昵称(输入用户名)")
        changed_username = input("请输入你要修改后的名称")
        if users_info.get(change_user):
            users_info[change_user]["name"] = changed_username
            print("修改成功")
            break
        else:
            print("查无此人，重来")
        # for i in users_info:
        #     if i[0] == change_user:
        #         i[0] = changed_username
        #         signal = 1
        #         print("修改成功")
        #         break
        # if signal == 0:
        #     print("查无此人，重来")
        #     continue
        # elif signal == 1:
        #     break


def modify_user_password():
    """
    Reset the user's password by entering their username
    :return: None
    """
    while True:
        change_user = input("请输入你要修改谁的密码")
        changed_password = "123456"
        if users_info.get(change_user):
            users_info["change_user"]["password"] = changed_password
            print("修改成功")
            break
        else:
            print("查无此人，重来")
        # signal = 0
        # for i in users_info:
        #     if i[0] == change_user:
        #         i[1] = changed_password
        #         signal = 1
        #         print("重置成功")
        #         break
        # if signal == 0:
        #     print("查无此人，重来")
        #     continue
        # elif signal == 1:
        #     break


def search_books():
    """
    Query books through their different attributes
    :return: None
    """
    while True:
        print("请输入要查询的类型：")
        print("1.书名")
        print("2.ISBN码")
        print("3.作者")
        print("4.类别")
        print("5.出版社")
        print("6.关键字")
        print("7.出版时间")
        print("8.退出查询")
        find_book = input("请输入你的选择")
        if (find_book == "1"
                or find_book == "2"
                or find_book == "3"
                or find_book == "4"
                or find_book == "5"
                or find_book == "6"
                or find_book == "7"):
            find_book_content = input("请输入你要查询的内容：")
            print("查询此书是否存在中-ing")
            book_find = True
            for i in range(len(book_info)):
                if book_info[i][int(find_book) - 1] == find_book_content:
                    print("此书存在，书籍信息为:", book_info[i])
                    book_find = False
                    break
            if book_find:
                print("此书不存在，请重新输入")
            else:
                break
        elif find_book == "8":
            break


def add_book():
    """
    Add books to the shopping cart by entering information about the books
    :return: None
    """
    new_book_name = input("请输入新书的名称:")
    new_book_ISBN = input("请输入新书的ISBN:")
    new_book_author = input("请输入新书的作者:")
    new_book_kind = input("请输入新书的类别:")
    new_book_press = input("请输入新书的出版社:")
    new_book_keyword = input("请输入新书的关键字:")
    new_book_time = input("请输入新书的出版时间:")
    new_book_money = input("请输入新书的价格:")
    # 判断新书是否重复
    new_book_existence = True
    for temp in book_info:
        if temp[1] == new_book_ISBN:
            print("ISBN号重复，添加失败")
            new_book_existence = False
            break
    if new_book_existence:
        book_info.append(
            [new_book_name, new_book_ISBN, new_book_author, new_book_kind,
            new_book_press, new_book_keyword, new_book_time,
            new_book_money])
        print("插入后所有的书籍:", book_info)


def delete_book():
    """
    Delete a book through its ISBN code
    :return: None
    """
    while True:
        delete_a_book = input("请输入要删除的书的ISBN码:")
        print("查询此书是否存在中-ing")
        #   book_find为是否查询到了书
        book_find = True
        for i in range(len(book_info)):
            if book_info[i][1] == delete_a_book:
                print("此书存在，书名为:", book_info[i][0])
                book_find = False
                deleted_book = book_info.pop(i)
                print("删除的书籍是：", deleted_book)
                print("删除后的剩余书籍有：", book_info)
                break
        if book_find:
            print("此书不存在，请重新输入")
        else:
            break


def change_book():
    """
    Confirm the book to be modified by using its ISBN code
    :return: None
    """
    while True:
        change_book_ISBN = input("请输入要修改的书籍的ISBN码:")
        print("查询此书是否存在中-ing")
        #   book_find为是否查询到了书
        book_find = True
        for i in range(len(book_info)):
            if book_info[i][1] == change_book_ISBN:
                print("此书存在，书名为:", book_info[i][0])
                book_find = False
                print("书籍的全部信息为：", book_info[i])
                while True:
                    print("请输入要改变的元素类型")
                    print("1.书名")
                    print("2.ISBN码")
                    print("3.作者")
                    print("4.类别")
                    print("5.出版社")
                    print("6.关键字")
                    print("7.出版时间")
                    print("8.价格")
                    change_book_select = input("请输入你的选择:")
                    if (change_book_select == "1"
                            or change_book_select ==
                            "2"
                            or change_book_select == "3"
                            or change_book_select == "4"
                            or change_book_select == "5"
                            or change_book_select == "6"
                            or change_book_select == "7"
                            or change_book_select == "8"):
                        change_book_info = input("请输入修改之后的内容：")
                        book_info[i][
                            int(change_book_select) - 1] = change_book_info
                        print("修改之后此书的内容为：", book_info[i])
                        break
                    else:
                        print("请重新输入正确的选择")
                break
        if book_find:
            print("此书不存在，请重新输入")
        else:
            break


def vip_recharge(user_username):
    """
    VIP recharge
    :param user_username:  当前用户的用户名
    :return: None
    """
    print("您现在是", users_info[user_username]["VIP"],"等级用户，提升VIP等级可以增加购书返利金额")
    recharge = input("若要进行充值，请输入1，否则将返回上级页面")
    if recharge == "1":
        recharge_money = input("请输入充值金额:")

        if not recharge_money.isdigit():
            print("请输入纯数字")
        elif recharge_money.startswith("0"):
            print("请输入正确格式的数字")
        else:
            users_info[user_username]["money"] = str(int(users_info[user_username]["money"]) + eval(recharge_money))
            #   计算VIP等级
            level = int(users_info[user_username]["money"])
            if level <= 100:
                users_info[user_username]["VIP"] = "ordinary"
            elif level <= 1000:
                users_info[user_username]["VIP"] = "silver"
            elif level <= 10000:
                users_info[user_username]["VIP"] = "gold"
            elif level <= 100000:
                users_info[user_username]["VIP"] = "platinum"
            else:
                users_info[user_username]["VIP"] = "masonry"
            print("充值之后你的VIP等级是:", users_info[user_username]["VIP"])


def shopping_cart_add(user_username):
    """
    shopping_cart_add
    :param user_username:  当前用户的用户名
    :return: None
    """
    print("------目前所有书籍--------")
    # 记录书籍一共有多少本，方便买书时判断书籍是否存在
    book_number = len(book_info)
    for i in range(book_number):
        print(i, " 书名:", book_info[i][0], " ISBN:", book_info[i][1], " 价格:",
            book_info[i][7])
    print("--------------------------------")
    buy_number = input("请输入你要购买的书籍的编号:")
    book_number -= 1
    # 判断一个字符串是否是数字
    if not buy_number.isdigit():
        print("请输入正确的编号")
    elif int(buy_number) > book_number:
        print("请输入正确的编号")
    else:

        buy_number = int(buy_number)
        users_info[user_username]["cart"].append(
            [book_info[buy_number][0], book_info[buy_number][1],
            int(book_info[buy_number][7])])
        print("现在你的购物车内的全部书籍为:", users_info[user_username]["cart"])


def shopping_cart_delete(user_username):
    """
    shopping_cart_delete
    :param user_username:  当前用户的用户名
    :return: None
    """
    # 删除的书不存在时返回
    delete_book_existence = True
    if not users_info[user_username]["cart"]:
        print("购物车为空,无可删除书籍")
    else:
        shopping_cart_delete = input("请输入你要删除的书籍的名字:")
        for i in range(len(users_info[user_username]["cart"])):
            if users_info[user_username]["cart"][i][0] == shopping_cart_delete:
                users_info[user_username]["cart"].pop(i)
                delete_book_existence = False
                break
        if delete_book_existence:
            print("要删除的书不存在")
        else:
            if not users_info[user_username]["cart"]:
                print("删除该书籍后购物车为空")
            else:
                print("删除该书籍后，购物车剩余书籍为:",users_info[user_username][10])


def rebate(user_username):
    """
    After the user settles the shopping cart, a random number within 20w will be used as a shopping rebate
    :param user_username:  当前用户的用户名
    :return: None
    """
    print("即将进行订单返利：")
    a = random.random() * 200000
    print("您的返利金额为:", a)
    users_info[user_username]["money"] = int(users_info[user_username]["money"]) + a
    print("返利后您的余额为:", users_info[user_username]["money"])


def shopping_cart_settlement(user_username):
    """
    shopping_cart_settlement
    :param user_username:  当前用户的用户名
    :return: NOne
    """
    total_amount = 0
    if not users_info[user_username]["cart"]:
        print("购物车为空，无需结算")
    else:
        temp_list = []
        # 将订单结算进订单列表
        ant = len(users_info[user_username]["cart"])
        for temp in users_info[user_username]["cart"]:
            total_amount += int(temp[2])
            temp_list.append(temp)
            ant -= 1
            if ant == 0:
                break
        print("您的订单总金额为:", total_amount)
        if total_amount > int(users_info[user_username]["money"]):
            print("余额不足")
        else:
            users_info[user_username]["money"] = int(
                users_info[user_username]["money"]) - total_amount
            temp_list.append("总金额:" + str(total_amount))
            users_info[user_username]["order"].append(temp_list)
            rebate(user_username)
            users_info[user_username]["cart"].clear()


def delete_order(user_username):
    """
    delete_order
    :param user_username:  当前用户的用户名
    :return: None
    """
    order_form_index = input("请输入要删除的订单编号:")
    if not order_form_index.isdigit():
        print("请输入正确的编号")
    else:
        order_form_index = int(order_form_index)
        users_info[user_username]["order"].pop(order_form_index)
        print("删除成功!")


def enter_personal_information(user_username):
    """
    enter_personal_information
    :param user_username:  当前用户的用户名
    :return: None
    """
    print("您的个人信息为：")
    print("VIP等级:", users_info[user_username]["VIP"])
    print("昵称:", users_info[user_username]["name"])
    print("真实姓名:", users_info[user_username]["real_name"])
    print("电话:", users_info[user_username]["phone"])
    print("地址:", users_info[user_username]["address"])
    print("邮编:", users_info[user_username]["postal"])
    print("余额:", users_info[user_username]["money"])
    print("生日:", users_info[user_username]["birthday"])
    print("个性签名:", users_info[user_username]["signature"])


def register_a_new_user():
    """
    Register a new user and perform a strength check on their password
    :return: None
    """
    user_username = input("请输入用户名:")
    while True:
        user_password = input("请输入密码(密码强度必须为中级及以上):")
        if len(user_password) > 16:
            print("你的密码长度过长，请重新输入")
            continue
        # 判断是否存在空格 或者 回车
        existence_space = False
        existence_enter = False
        # 判断密码强度
        password_strength = [0, 0, 0, 0]
        for i in user_password:
            if i == " ":
                existence_space = True
                break
            elif i == "\n":
                existence_enter = True
                break
            else:
                if i.isupper():
                    password_strength[0] = 1
                elif i.islower():
                    password_strength[1] = 1
                elif i.isdigit():
                    password_strength[2] = 1
                else:
                    password_strength[3] = 1
        if existence_space:
            print("你的密码中存在空格，请重新输入")
        elif existence_enter:
            print("你的密码中存在回车，请重新输入")
        elif len(user_password) <= 8 or sum(password_strength) <= 1:
            print("你的密码是初级密码，请重新输入")
        elif 16 >= len(user_password) >= 12 and sum(password_strength) == 4:
            print("你的密码是高级密码，可以注册")
            break
        else:
            print("你的密码是中级密码，可以注册")
            break
    user_VIP = "ordinary"
    user_nickname = input("请输入昵称:")
    user_name = input("请输入姓名:")
    user_phone = input("请输入电话:")
    user_address = input("请输入地址:")
    user_postal_code = input("请输入邮编:")
    user_money = "0"
    user_birthday = input("请输入生日:")
    user_personal_signature = input("请输入个性签名")
    #   默认购物车和订单为空
    # 判断用户名是否已存在

    if users_info.get(user_username):
        print("用户名已存在，请换一个")
        username_existence = False
    else:
        users_info[user_username] = {
                                    "name": user_nickname, "password": user_password, "VIP": user_VIP,
                                    "real_name": user_name, "address": user_address, "birthday": user_birthday,
                                    "phone": user_phone, "postal": user_postal_code,
                                    "signature": user_personal_signature, "money": user_money, "cart": [], "order": []
        }
        print("注册成功！内容为：", users_info[user_username])


while True:
    # 1. 图书管理系统的页面
    print("--------------欢迎使用图书管理系统------------------")
    print("请选择你的身份：")
    print("1. 管理员")
    print("2. 普通用户")
    user_index_input = input("请输入：")
    if user_index_input == "1":
        # 管理员身份
        while True:
            print("欢迎来到管理员页面")
            print("请做出你的选择")
            # admin ?????
            print("1. 登录")
            print("2. 忘记密码")
            print("3. 返回选择登入用户界面")
            admin_input = input("请做出你的选择：")
            if admin_input == "1":
                # 判断是否登入失败
                admin_page_signal = 0
                while True:
                    admin_username_login_input = input("请输入你的用户名:")
                    admin_password_login_input = input("请输入你的密码:")
                    # 遍历管理员表
                    for admin in admin_info:
                        # 判断用户名是否相等
                        if admin[0] == admin_username_login_input:
                            # 判断密码是否相等
                            if admin[1] == admin_password_login_input:
                                # 管理员用户登陆成功
                                admin_page_signal = 1
                                print("登陆成功")
                                while True:
                                    print("请选择你要做的操作:")
                                    print("1.管理用户信息")
                                    print("2.退出登录")
                                    admin_logged_input = input("请输入你的选择:")
                                    if admin_logged_input == "1":
                                        break
                                    elif admin_logged_input == "2":
                                        break
                                    else:
                                        print("请重新输入")
                                if admin_logged_input == "1":
                                    print("1.修改用户名")
                                    print("2.重置密码")
                                    print("3.管理图书")
                                    while True:
                                        # 进入管理员界面后的操作
                                        admin_logged_operation = input("请输入你要选择的操作:")
                                        if admin_logged_operation == "1":
                                            modify_user_name()
                                        elif admin_logged_operation == "2":
                                            modify_user_password()
                                            # admin_logged_operation 等于3时 结束操作循环 进入图书管理
                                        elif admin_logged_operation == "3":
                                            break
                                        else:
                                            print("请正确进行输入")
                                    if admin_logged_operation == "3":
                                        while True:
                                            print("1.增加新书")
                                            print("2.根据ISBN号删除书籍")
                                            print("3.根据ISBN号修改书籍")
                                            print("4.查找书籍")
                                            print("5.退出")
                                            admin_logged_new_operation = input("请输入你的选择:")
                                            if admin_logged_new_operation == "1":
                                                add_book()
                                            elif admin_logged_new_operation == "2":
                                                delete_book()
                                            elif admin_logged_new_operation == "3":
                                                change_book()
                                            elif admin_logged_new_operation == "4":
                                                search_books()
                                            elif admin_logged_new_operation == "5":
                                                print("进程已结束")
                                                break
                                elif admin_logged_input == "2":
                                    print("成功退出登入")
                                else:
                                    print("请正确进行输入:")

                    if admin_page_signal == 1:
                        break
                    print("登录失败，请重新登录")

                break
            elif admin_input == "2":
                print("忘记密码也没用，请重新选择")
            elif admin_input == "3":
                break
            else:
                # 重新选择
                print("请重新选择")
        # break
    elif user_index_input == "2":
        while True:
            # 用户身份
            print("普通用户页面")
            print("--------------------------------")
            print("1.登入")
            print("2.注册")
            print("3.退出到选择登入用户界面")
            user_operation = input("请输入你要进行的操作:")
            if user_operation == "1":
                user_username = input("请输入用户名:")
                user_password = input("请输入密码:")
                # 登入失败时在控制台打印
                login_status = True
                if users_info.get(user_username):
                    if users_info[user_username]["password"] == user_password:
                        print("登入成功！")
                        while True:
                            print("1.退出登入")
                            print("2.VIP充值")
                            print("3.图书查询")
                            print("4.购物车")
                            print("5.订单管理")
                            print("6.查看个人信息")
                            user_login_input = input("请输入你要进行的操作:")
                            if user_login_input == "1":
                                break
                                print("退出成功")
                            elif user_login_input == "2":
                                vip_recharge(user_username)
                            elif user_login_input == "3":
                                search_books()
                            elif user_login_input == "4":
                                print("当前所有图书为：")
                                for temp in book_info:
                                    print(temp)
                                if not users_info[user_username]["cart"]:
                                    print("您的购物车当前为空")
                                else:
                                    print("您的购物车内有以下书籍:", users_info[user_username]["cart"])
                                while True:
                                    print("1.添加书籍")
                                    print("2.删除购物车内书籍")
                                    print("3.结算")
                                    print("4.退出")
                                    shopping_cart = input("请输入你要执行的操作:")
                                    if shopping_cart == "1":
                                        shopping_cart_add(user_username)
                                    elif shopping_cart == "2":
                                        shopping_cart_delete(user_username)
                                    elif shopping_cart == "3":
                                        shopping_cart_settlement(user_username)
                                    elif shopping_cart == "4":
                                        print("退出")
                                        break
                                    else:
                                        print("请重新输入正确的选择！")
                            elif user_login_input == "5":
                                print("您当前的所有订单为:")
                                for i in range(len(users_info[user_username]["order"])):
                                    print(i, ":", users_info[user_username]["order"][i])
                                while True:
                                    print("1.删除订单")
                                    print("2.返回")
                                    order_form = input("请输入您的选择")
                                    if order_form == "1":
                                        if not users_info[user_username]["order"]:
                                            print("当前无订单可以删除")
                                        else:
                                            delete_order(user_username)
                                    elif order_form == "2":
                                        break
                                    else:
                                        print("请重新输入正确的选择")
                            elif user_login_input == "6":
                                enter_personal_information(user_username)
                            else:
                                print("请重新进行正确的输入")
                    else:
                        print("用户名或密码错误，请重新输入")
            elif user_operation == "2":
                register_a_new_user()
            elif user_operation == "3":
                break
            else:
                print("请重新进行正确的输入")
    else:
        print("请重新输入")
