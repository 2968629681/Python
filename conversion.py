import os
# import pythoncom
# from threading import Thread
from comtypes import client
from multiprocessing import Process,Pool


def word_to_pdf(input_path, output_path):
    # 创建 Word 应用对象
    word_app = client.CreateObject('Word.Application')

    # 启动 Word 应用程序（可见性设置为 False）
    word_app.Visible = False

    try:
        # 打开 Word 文档
        doc = word_app.Documents.Open(input_path)

        # 将 Word 文档保存为 PDF 格式
        doc.SaveAs(output_path, FileFormat=17)  # 文件格式为 PDF

        # 关闭 Word 文档
        doc.Close()

        print(f"已将 {input_path} 转换为 {output_path}")
    except Exception as e:
        print(f"转换失败: {e}")
    finally:
        # 退出 Word 应用程序
        word_app.Quit()


def batch_word_to_pdf(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".docx") or filename.endswith(".doc"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.rsplit(".", 1)[0] + ".pdf")
            word_to_pdf(input_path, output_path)


def first():
    # print("First")
    # pythoncom.CoInitialize()
    input_folder = r"C:\Users\29686\Desktop\python\实验报告\猫狗识别实验报告"  # 输入 Word 文档所在文件夹路径
    output_folder = r"C:\Users\29686\Desktop\python\实验报告\猫狗识别实验报告\PDF"  # 输出 PDF 文件的保存路径
    batch_word_to_pdf(input_folder, output_folder)


def second():
#     print("second")
#     pythoncom.CoInitialize()
    input_folder = r"C:\Users\29686\Desktop\python\实验报告\图书管理系统实验报告"  # 输入 Word 文档所在文件夹路径
    output_folder = r"C:\Users\29686\Desktop\python\实验报告\图书管理系统实验报告\PDF"  # 输出 PDF 文件的保存路径
    batch_word_to_pdf(input_folder, output_folder)


def third():
#     print("Third")
#     pythoncom.CoInitialize()
    input_folder = r"C:\Users\29686\Desktop\python\实验报告\招聘网站职位信息爬虫系统实验报告"  # 输入 Word 文档所在文件夹路径
    output_folder = r"C:\Users\29686\Desktop\python\实验报告\招聘网站职位信息爬虫系统实验报告\PDF"  # 输出 PDF 文件的保存路径
    batch_word_to_pdf(input_folder, output_folder)




if __name__ == '__main__':
    # thread1 = Thread(target=first)
    # thread2 = Thread(target=second)
    # thread3 = Thread(target=third)
    # thread1.start()
    # thread2.start()
    # thread3.start()

    pool = Pool(3)

    # p3 = Process(target=func2)
    pool.apply_async(func=first)
    pool.apply_async(func=second)
    pool.apply_async(func=third)
    # async:异步
    pool.close()
    pool.join()