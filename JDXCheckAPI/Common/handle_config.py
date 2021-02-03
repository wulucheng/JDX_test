"""
项目的名称: main.py
文件的名称： handle_config 
文件时间： 2021-01-28 15:00
"""


from configparser import ConfigParser
import os

from Common.handle_path import conf_dir


class HandleConfig(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


file_path = os.path.join(conf_dir, "config.ini")
conf = HandleConfig(file_path)



# if __name__ == '__main__':
#     conf = HandleConfig("config.ini")
#     print(conf.get("log", "name"))