import requests
import re
import time
import threading

mutex = threading.Lock()
i = 0


def download(picture_links, headers):
    while picture_links:
        global i
        mutex.acquire()
        link = picture_links.pop()
        mutex.release()

        time.sleep(0.2)
        try:
            r = requests.get(url=link, headers=headers)
        except Exception as ret:
            print(ret)
        with open(".\pictures\%s.jpg" % i, "wb") as f:
            f.write(r.content)
        print("当前正在爬取第%d张!!" % i)
        mutex.acquire()
        i += 1
        mutex.release()


def main():
    # 1.获取cookies
    # cookies = {}
    # with open("虎牙颜值cookies.txt", "r") as f:  # 打开事先存好的cookies文件
    #     for line in f.read().split(";"):  # 按照;分割
    #         name, value = line.split("=", 1)  # 然后按照等号分割开，使用参数1代表分割成为两份
    #         cookies[name] = value  # 然后在cookies字典里面设置值
    # 2.设置请求头代理
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    # 3.获取网页源文件
    url = "https://www.huya.com/g/2168"
    r = requests.get(url=url, headers=headers)
    # 4.正则获取网页图片链接
    picture_links = re.findall(r'data-original="(.*?)\?.*"', r.content.decode("utf-8"))
    print(picture_links)
    print("一共有%d张图片" % len(picture_links))
    # 5.下载网页图片链接里面的内容并创建图片保存
    t1 = threading.Thread(target=download, args=(picture_links, headers))
    t2 = threading.Thread(target=download, args=(picture_links, headers))
    t3 = threading.Thread(target=download, args=(picture_links, headers))
    t4 = threading.Thread(target=download, args=(picture_links, headers))
    t5 = threading.Thread(target=download, args=(picture_links, headers))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()


if __name__ == "__main__":
    main()
