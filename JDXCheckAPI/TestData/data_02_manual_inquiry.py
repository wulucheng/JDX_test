"""
项目的名称: main.py
文件的名称： 02_manual_inquiry 
文件时间： 2021-01-29 16:58
"""

import requests
import os

from Common.handle_txt import read_txt_as_list

# data_02 = read_txt_as_list("02_Manual_Inquiry.txt")
# print(len(data_02))
# print(data_02)

data_manual_inquiry = [
                        {'param': 36047, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 36300, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 32068, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 34701, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 32068, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 36045, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 27627, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 34448, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 27664, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 26983, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 32835, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 35585, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 27664, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 32047, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 32291, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 35548, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 28684, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 25935, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 35582, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 36044, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 32292, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'},
                        {'param': 32292, 'name': '人工询价', 'type': '质检入参', 'url': '/app/inspection/report/create/report/default'}
                      ]






# url = "http://sjapi.aihuishou.com/jdx-qa-service/app/inspection/report/create/report/default"
#
# payload={"productId":34701}
# headers = {
#   'Access-Token': '42f819c50a280a4a183167aba9966596',
#   'App-ID': 'jdx470738'
# }
#
# response = requests.request("GET", url, headers=headers, params=payload)
#
# print(response.text)
