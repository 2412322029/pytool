#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/28 13:17
# @Author  : lolik
# @File    : BASE64.py
# @Software: PyCharm

def bytes2base64(by: bytes):
    data = ""
    result = ""
    coded = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for i in by:
        i = "".join(f"{i:08b}")
        data += i
    data += (6 - len(data) % 6) * "0"
    for x in range(0, len(data), 6):
        ac = data[x:x + 6]
        res = coded[int("0b" + ac, 2)]
        result += res
    result += "=="
    return result


if __name__ == '__main__':
    import os
    png = "img.png"
    if os.path.exists(png):
        with open(png, "rb") as f:
            a = f.read()
        print(bytes2base64(a))
    else:
        print("缺少 "+png)
