"""
项目的名称: main.py
文件的名称： handle_path 
文件时间： 2021-01-28 15:01
"""


import os

#获取当前文件夹所在的路径， E:\Python文件\PhoneCheckAPI
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#获取Conf文件所在的路径
conf_dir = os.path.join(base_dir, "Conf")

#获取测试数据所在的路径
data_dir = os.path.join(base_dir, "TestData")

#获取log文件所在的路径
logs_dir = os.path.join(os.path.join(base_dir, "Outputs"), "logs")





