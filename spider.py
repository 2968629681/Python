import requests, os, time
from lxml import etree


# e:element:标签
# tree: 树

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


url = "https://www.ibiquges.org/xiaoshuodaquan/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54"
}
res = requests.get(url=url, headers=headers)
ele = etree.HTML(res.text)
booknames = ele.xpath("//div[@class='novellist']/ul/li/a/text()")
booknurls = ele.xpath("//div[@class='novellist']/ul/li/a/@href")
while booknames == []:
    res = requests.get(url=url, headers=headers)
    ele = etree.HTML(res.text)
    booknames = ele.xpath("//div[@class='novellist']/ul/li/a/text()")
    booknurls = ele.xpath("//div[@class='novellist']/ul/li/a/@href")
for i in range(len(booknurls)):
    res1 = requests.get(url=booknurls[i], headers=headers)
    res1 = res1.content.decode("utf-8")
    ele1 = etree.HTML(res1)
    chapter_author = ele1.xpath("//div[@id='info']/p/text()")
    while chapter_author == []:
        res1 = requests.get(url=booknurls[i], headers=headers)
        res1 = res1.content.decode("utf-8")
        ele1 = etree.HTML(res1)
        chapter_author = ele1.xpath("//div[@id='info']/p/text()")
    mkdir('./' + booknames[i] + "  " + chapter_author[0])
    chapter_names = ele1.xpath("//div[@id='list']/dl/dd/a/text()")
    chapter_urls = ele1.xpath("//div[@id='list']/dl/dd/a/@href")
    chapter_urls = ["https://www.ibiquges.org" + i for i in chapter_urls]
    for j in range(len(chapter_urls)):
        res2 = requests.get(url=chapter_urls[j], headers=headers)
        res2 = res2.content.decode("utf-8")
        ele2 = etree.HTML(res2)
        novel_content = ele2.xpath("//div[@id='content']/text()")
        novel_title = ele2.xpath("//div[@class='bookname']/h1/text()")
        while novel_title == []:
            res2 = requests.get(url=chapter_urls[j], headers=headers)
            res2 = res2.content.decode("utf-8")
            ele2 = etree.HTML(res2)
            novel_content = ele2.xpath("//div[@id='content']/text()")
            novel_title = ele2.xpath("//div[@class='bookname']/h1/text()")
        print(novel_title)
        f = open('./' + booknames[i] + "  " + chapter_author[0] + './' + novel_title[0] + ".txt", mode='a',
                encoding="utf-8")
        f.writelines('         ' + novel_title[0] + '\n\n\n')
        for temp in novel_content:
            f.writelines(temp)
        f.close()
