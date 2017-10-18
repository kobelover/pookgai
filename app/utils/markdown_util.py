# -*- coding: utf-8 -*-
import mistune
import time
import os

# TODO 对上传的模板进行 按时间存储在upload 目录下面
PWD = os.path.split(os.path.realpath(__file__))[0]
UPLOAD = "static\\uploads"

markdown = mistune.Markdown(escape=True, hard_wrap=True)


def ymd():
    localtime = time.localtime(time.time())
    return localtime.tm_year, localtime.tm_mon, localtime.tm_mday


def mkdir_ymd():
    path = os.path.join(str(PWD), str(UPLOAD), str(ymd()[0]), str(ymd()[1]), str(ymd()[2]))
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def readMD(file):
    with open(file, 'rt', encoding='utf-8') as f:
        data = f.read()  # <class 'str'>
        str = markdown(data)

    file_name = os.path.join(mkdir_ymd(), "md.html")

    with open(file_name, 'xt', encoding='utf-8') as f:
        f.write(str, )


def saveHTMl(str):
    # TODO
    pass


if __name__ == '__main__':
    file = 'static\\upload\\mk.md'
    readMD(file)
    # mkdir_ymd("1.html")
