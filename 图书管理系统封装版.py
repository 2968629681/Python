admi_info = ["xx", 'xx']
# 1. 账号 2.密码
users_info = [
    ['xxx', 'xxx', '普通VIP', '张奥凯', '13145200803', '2002-0803', '666', '山西省临汾市', '041000',
    '我爱学习python嘿嘿！', "4"]
    # 1.账号 2.密码  3.VIP等级 4.真实姓名  5.电话号   6.生日         7.身份证号          8.地址        9.邮编    10.个性签名  11.累计充值金额
]
book_info = [
    ["三国演义", "5201314", "罗贯中", "人民文学出版社", "1953.11", "历史", "64-80万字数", "959页", "78"],
    ["西游记", "1314520", "吴承恩", "花城出版社", "2003.08", "神魔", "87万字数", "627页", "99"]
    # 1.书名   2.SIBN   3.作者    4.出版社   5.出版时间  6.内容类型   7.字数     8.页数    9.价格（元）
]
shopping_info = [

]


# 主页界面
def index_page():
    print("----------------欢迎您!-----------------")
    print("------------来到图书管理系统--------------")
    # 图书管理系统的页面设计
    adim_exit_input = "no"
    print("请选择你的身份：1.管理员   2.用户")
    # 告知使用者选择身份
    users_index_input = input("请输入你的身份：")
    return users_index_input


# 管理员界面
def admin_page():
    print("欢迎来到管理员界面,请选择你要进行的操作：\n1.登录  \n2.忘记密码  \n3.重置密码  ")
    # 提示管理员进行操作选择
    admin_option_input = input()
    return admin_option_input


# 管理员登录逻辑
def admin_login_logic(admin_username_input, admin_password_input):
    if admin_username_input == admi_info[0] and admin_password_input == admi_info[1]:
        # 判断账号密码是否与管理员列表中的信息一致
        # 提示管理员账号密码与列表中的一致
        return True
    return False


# 管理员登录界面
def admin_login_page():
    print("------欢迎你，来到登录界面！------")
    # 提示管理员来到登录页界面
    # 让管理员登录界面进行循环
    admi_code_input = input("请输入你的账号：")
    # 提示管理员输入账号
    admi_password_input = input("请输入你的密码：")
    # 提示管理员输入密码
    if admin_login_logic(admi_code_input, admi_password_input):
        # 登录成功
        print("------恭喜您！登录成功！！------")
        return True
    else:
        print("------恭喜您！登录失败！！------")
        return False


# 管理员主页逻辑
def admin_index_logic(admi_input):
    if admi_input == "1":
        # 判断管理员是否选择用户信息管理操作
        return 1

    elif admi_input == "2":
        return 2

    elif admi_input == "3":
        return 3

    else:
        return False


# 管理员退出登录
def admin_logout():
    """
    :return: boolean，if False,then logout.
    """
    return True


# 管理员主页页面
def admin_index_page():
    print("请选择你要进行的操作： 1.管理用户信息  2.管理图书  3.退出登录")
    # 提示管理员选择要进行的操作
    admi_input = input()
    # ---------------------------------------------------------用户信息管理-------------------------------------------
    if admin_index_logic(admi_input) == 1:
        admin_manageuser_page()

    if admin_index_logic(admi_input) == 2:
        admin_managebook_page()
        print("------欢迎进入图书管理界面！------")

    if admin_index_logic(admi_input) == 3:
        if admin_logout():
            print("------退出登录！------")
            index_page()
        else:
            print("没退成")


# 修改用户名
def change_username(admi_change_code_input, newname):
    # 提示管理员输入要修改的用户名
    for user in users_info:
        if user[0] == admi_change_code_input:
            # 判断用户库中是否存在输入用户名
            # 提示管理员输入新的用户名
            user[0] = newname
            # 修改信息
            print(users_info)
            return True


# 修改密码
def change_password(admi_change_code_input):
    # 提示管理员输入要修改的密码
    for user in users_info:
        if user[0] == admi_change_code_input:
            # 判断用户库中是否存在输入用户名
            user[1] = "123456"
            # 修改信息

            return True


# 管理员管理用户逻辑函数
def admin_manageuser_logic(admi_users_option_input):
    if admi_users_option_input == "1":
        old_name, new_name = admin_page_manageuser_middleware(1)
        if change_username(old_name, new_name):
            return True
    elif admi_users_option_input == "2":
        username = admin_page_manageuser_middleware(2)
        if change_password(username):
            return True


# 管理员管理用户的逻辑函数和视图函数的中间件
def admin_page_manageuser_middleware(user_choice):
    if user_choice == 1:
        # 修改用户名
        old_name = input("请输入要修改的用户的用户名：")
        new_name = input("请输入新的用户名：")
        return old_name, new_name
    if user_choice == 2:
        # 修改密码
        username = input("请输入要修改的用户的用户名：")
        return username


# 管理员管理用户的视图函数
def admin_manageuser_page():
    print("------欢迎进入用户管理界面！------")
    # 循环用户管理界面
    print("请选择你要进行的操作：1.修改用户的用户名 2.修改用户的密码 3. 退出系统")
    # 提示管理员选择进行的操作
    admi_users_option_input = input()
    if admi_users_option_input == "3":
        admin_index_page()
    # 输入要进行的操作
    if admin_manageuser_logic(admi_users_option_input):
        print('修改成功')
        admin_manageuser_page()
    else:
        print('修改失败')
        admin_index_page()


# 添加图书
def add_book():
    book_info.append(list(admin_page_managebook_middleware(1)))
    return True


# 删除图书
def del_book():
    book_ISBN = admin_page_managebook_middleware(2)
    for book in book_info:
        if book[1] == book_ISBN:
            book_info.remove(book)
            return True


# 修改图书
def change_book():
    book_ISBN = admin_page_managebook_middleware(3)
    for book in book_info:
        if book[1] == book_ISBN:
            print(book)
            user_choice = admin_page_managebook_middleware(4)
            book[user_choice[0] - 1] = user_choice[1]
            return True
    return False


# 查询图书
def select_book():
    bookISBN = admin_page_managebook_middleware(5)
    for book in book_info:
        if book[1] == bookISBN:
            return book
    return False


def admin_page_managebook_middleware(user_choice):
    # 增加图书的用户输入
    if user_choice == 1:
        bookname = input("请输入书名")
        bookISBN = input("请输入ISBN")
        bookauthor = input("请输入作者")
        bookpublisher = input("请输入出版社")
        bookpublish_time = input("请输入出版时间")
        booktype = input("请输入内容类型")
        bookcharsize = input("请输入字数")
        bookpagesize = input("请输入页数")
        bookprice = input("请输入价格")
        booksales = input("请输入已售卖")
        bookresi = input("请输入库存")
        return bookname, bookISBN, bookauthor, bookpublisher, bookpublish_time, booktype, bookcharsize, bookpagesize, bookprice, booksales, bookresi
    # 删除图书的用户输入
    elif user_choice == 2:
        bookISBN = input("请输入要删除的图书的ISBN号")
        return bookISBN
    # 修改图书功能的用户输入
    elif user_choice == 3:
        bookISBN = input("请输入要修改的图书的ISBN")
        return bookISBN
    # 修改图书的某一项的用户输入
    elif user_choice == 4:
        print("请输入要修改哪一项")
        userchoice = input(
            "请输入你要修改的信息序号：\n1.书名\n2.ISBN\n3.作者\n4.出版社\n5.出版时间\n6.内容类型\n7.字数\n8.页数\n9.价格（元\n10.已售\n11.库存\n")
        new_info = input("请输入要改成啥?")
        return int(userchoice), new_info
    # 用户查询图书输入ISBN号
    elif user_choice == 5:
        return input("请输入要查询的图书的ISBN号：")


# 管理员管理图书逻辑函数
def admin_managebook_logic(admi_book_option_input):
    if admi_book_option_input == "1":
        # 增加图书
        if add_book():
            return True

    elif admi_book_option_input == "2":
        # 删除图书
        if del_book():
            return True

    elif admi_book_option_input == "3":
        # 修改图书
        if change_book():
            return True

    elif admi_book_option_input == "4":
        # 查询图书
        result = select_book()
        if result:
            return result
        else:
            return False


# 管理员管理图书视图函数
def admin_managebook_page():
    print("------欢迎进入图书管理界面！------")
    # 循环用户管理界面
    print("请选择你要进行的操作：1.添加图书 2.删除图书 3.修改图书 4.查询图书")
    # 提示管理员选择进行的操作
    admi_book_option_input = input()
    # 输入要进行的操作
    managebook_result = admin_managebook_logic(admi_book_option_input)
    if type(managebook_result) == "list":
        print(managebook_result)
    elif managebook_result:
        print('修改成功')
        admin_index_page()
    else:
        print('修改失败')
        admin_index_page()


# 用户主页视图函数
def user_index_page():
    print("欢迎来到用户界面,请选择你要进行的操作\n1.登录\n2.注册\n3.忘记密码\n")
    # 提示用户进行操作选择
    users_option_input = input()
    # if users_option_input == "1":
    #     user_login_page()
    # elif users_option_input == "2":
    #     user_register_page()
    return users_option_input


# 用户登录逻辑
def user_login_logic(user_username_input, user_password_input):
    for temp in users_info:
        if user_username_input == temp[0] and user_password_input == temp[1]:
            # 判断账号密码是否与管理员列表中的信息一致
            # 提示管理员账号密码与列表中的一致
            return True
    return False


# 用户登录页面
def user_login_page():
    print("------欢迎你，来到登录界面！------")
    # 提示用户来到登录页界面
    user_code_input = input("请输入你的账号：")
    # 提示用户输入账号
    user_password_input = input("请输入你的密码：")
    # 提示用户输入密码
    if user_login_logic(user_code_input, user_password_input):
        # 登录成功
        print("------恭喜您！登录成功！！------")
        user_opr_page()
        return True
    else:
        print("------登录失败！！------")
        user_index_page()
        return False


# 注册视图函数
def user_register_page():
    print("------欢迎来到注册界面！------")
    # 提示用户进入到了注册界面
    # 创建一个空列表，用来存放注册的新用户的信息
    username = input("请输入你的账号：")
    password = input("请输入你的密码：")
    VIP = input("请输入你的VIP等级：")
    realname = input("请输入你的真实姓名：")
    tele = input("请输入你的电话号：")
    birth = input("请输入你的生日：")
    ID_card = input("请输入你的身份证号：")
    addr = input("请输入你的地址：")
    postcode = input("请输入你的邮编：")
    introduce = input("请输入你的个性签名：")
    new_user = [username, password, VIP, realname, tele, birth, ID_card, addr, postcode, introduce]
    if user_register_logic(new_user):
        print("------注册成功！------")
        return True
    else:
        print("------注册失败！------")
        return False


# 用户注册的逻辑函数
def user_register_logic(new_user):
    users_info.append(new_user)
    return True


# 忘记密码逻辑函数
def forgot_password_logic(username, new_passwd):
    for user in users_info:
        if user[0] == username:
            user[1] = new_passwd
            return True
    return False


# 忘记密码视图函数
def forgot_password_page():
    print("------欢迎来到忘记“密码界面”!!------")
    print("请输入账号:")
    # 提示用户输入账号
    username = input("请输入你的账号：")
    new_passwd = input("请输入你的新密码：")
    if forgot_password_logic(username, new_passwd):
        print("修改成功")
        return True
    else:
        print("修改失败")
        return False


# 用户主页逻辑函数
def user_index_logic():
    user_option_input = user_index_page()
    if user_option_input == "1":
        # 登录页面
        login_status = user_login_page()
        return login_status
    elif user_option_input == "2":
        # 注册页面
        register_status = user_register_page()
        user_index_logic()
    elif user_option_input == "3":
        # 忘记密码
        forgot_status = forgot_password_page()
        user_index_logic()
        # return forgot_status


# 查询图书的视图函数

# 1.书名   2.ISBN   3.作者    4.出版社   5.出版时间  6.内容类型   7.字数     8.页数    9.价格（元）
# 根据书名查书
def select_by_bookname(bookname):
    books = []
    for book in book_info:
        if book[0] == bookname:
            books.append(book)
    return books


# 根据出版社查书
def select_by_publisher(bookpublisher):
    books = []
    for book in book_info:
        if book[3] == bookpublisher:
            books.append(book)
    return books


# 根据ISBN查书
def select_by_ISBN(bookISBN):
    for book in book_info:
        if book[1] == bookISBN:
            return [book]


# 根据作者查书
def select_by_author(bookauthor):
    books = []
    for book in book_info:
        if book[2] == bookauthor:
            books.append(book)
    return books


# 根据出版时间查书
def select_by_publishtime(bookpublishtime):
    books = []
    for book in book_info:
        if book[4] == bookpublishtime:
            books.append(book)
    return books


# 格式化打印图书
def print_book_info(books):
    # 1.书名   2.ISBN   3.作者    4.出版社   5.出版时间  6.内容类型   7.字数     8.页数    9.价格（元）
    print("序号\t书名\tISBN\t作者\t出版社\t出版时间\t内容类型\t字数\t页数\t价格（元）\t")
    for index, book in enumerate(books):
        print(str(index + 1) + '\t' + book[0] + '\t' + book[1] + '\t' + book[2] + '\t' +
            book[3] + '\t' + book[4] + '\t' + book[5] + '\t' +
            book[6] + '\t' + book[7] + '\t' + book[8] + '\t')


def select_book_page():
    input("请输入要查询书籍的 书名 或 SIBN 或者 出版社 或 作者 或 出版时间 ：")
    print("俺们有这么多查询方式，请选择你用哪种？")
    print("1. 书名")
    print("2. ISBN")
    print("3. 出版社")
    print("4. 作者")
    print("5. 出版时间")
    print("俺们有这么多查询方式，请选择你用哪种？")
    user_choice = input("请做出你的选择：")
    if user_choice == "1":
        bookname = input("请输入书名：")
        selected_books = select_by_bookname(bookname)
    elif user_choice == "2":
        bookISBN = input("请输入ISBN：")
        selected_books = select_by_ISBN(bookISBN)
    elif user_choice == "3":
        bookpublisher = input("请输入出版社：")
        selected_books = select_by_publisher(bookpublisher)
    elif user_choice == "4":
        bookauthor = input("请输入作者：")
        selected_books = select_by_author(bookauthor)
    elif user_choice == "5":
        bookpublishtime = input("请输入出版时间：")
        selected_books = select_by_publishtime(bookpublishtime)
    else:
        selected_books = ['', '', '', '', '', '', '', '', '', ]
    print_book_info(selected_books)
    return True


# 购买页面
def buy_page():
    print("------欢迎来到购买图书界面！！------")
    print("请选择您是要输入购买书籍的 书名 还是 ISBN: ")
    print("1. 书名")
    print("2. ISBN")
    users_book_option_input = input("请输入: ")
    if users_book_option_input == "1":
        # 1. 根据书名查书
        book_name = input("请输入书名：")
        books = select_by_bookname(book_name)
        print("请选择你要购买的图书的序号：")
        print_book_info(books)
        book_index = input("请选择：")
        shopping_info.append(books[int(book_index) - 1])
        return True
    elif users_book_option_input == "2":
        # 1. 根据书名查书
        book_ISBN = input("请输入ISBN：")
        books = select_by_ISBN(book_ISBN)
        shopping_info.append(books[0])
        return True
    return False


# 用户操作页面视图函数
def user_opr_page():
    users_option_input = input("请选择你要进行的操作:\n1.查询图书\n2.购买图书\n3.充值\n4.退出登录\n")
    if users_option_input == "1":
        # 查询图书
        select_status = select_book_page()
        user_opr_page()
        return select_status
    elif users_option_input == "2":
        # 购买图书
        buy_status = buy_page()
        if buy_status:
            print("购买成功")
        else:
            print("购买失败")
        user_opr_page()
    elif users_option_input == "4":
        main()


def main():
    index_input = index_page()
    if index_input == "1":
        # 管理员登录
        if admin_login_page():
            # 登录成功
            admin_index_page()
        else:
            # 登录失败
            main()
    elif index_input == "2":
        user_index_logic()


main()
