"""
项目的名称: main.py
文件的名称： handle_txt 
文件时间： 2021-02-01 14:37
"""

import os
import json

from Common.handle_path import data_dir


def read_txt_as_list(file_name):
    # 默认file_name是来自于TestData下面的text文件
    file_path = os.path.join(data_dir, file_name)
    with open(file_path) as fs:
        data = fs.readlines()
        data_list = []
        for item in data:
            item.strip("\\n")
            data_dict = json.loads(item)
            data_list.append(data_dict)
    return data_list
