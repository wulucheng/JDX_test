
"""
项目的名称: main.py
文件的名称： 尝试 
文件时间： 2021-01-28 16:53
"""

import requests


import contextlib

original_data = open("C:\\Users\\115579\\Desktop\\data\\split.txt", "r", encoding="utf-8")
content = original_data.readlines()
print(len(content))


for item in content:
    if item.find("/app/inspection/report/create/report/default") != -1:
        with open("C:\\Users\\115579\\Desktop\\data\\02_Manual_Inquiry.txt", "a") as file_02:
            file_02.write(item)
    elif item.find("/app/inspection/report/receive/hardware/android") != -1:
        with open("C:\\Users\\115579\\Desktop\\data\\03_Android_USB_Check.txt", "a") as file_03:
            file_03.write(item)
    elif item.find("/app/inspection/report/create/report/by-sku") != -1:
        with open("C:\\Users\\115579\\Desktop\\data\\04_OCR_IMEI_Inquriy.txt", "a") as file_04:
            file_04.write(item)
original_data.close()