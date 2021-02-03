"""
项目的名称: main.py
文件的名称： handle_request 
文件时间： 2021-01-28 16:29
"""

import requests
import json
import jsonpath

from Common.my_logger import logger
from Common.handle_config import conf
 

def send_requests(method, url, header=1, data=None, token=None, verify = False):
    """
    :param method: 请求的方法，POST或者GET
    :param url: 请求的地址，可以缺省 https://sjapi.aihuishou.com/
    :param header: 做了封装处理，1的时候只需要1个header，5的时候需要5个header
    :param data: 请求参数
    :param token: 请求的token
    :param verify: 默认是False，要不然会报SSL的错误
    :return:
    """
    logger.info("*********** 发起一次HTTP请求 *************")
    logger.info("请求方法为：{}".format(method))
    full_url = __handle_url(url)
    full_header = __handle_header(header, token)
    logger.info("请求url为：{}".format(full_url))
    logger.info("请求数据为：{}".format(data))
    # 根据请求类型，调用请求方法
    method = method.upper()  # 大写处理
    if method == "GET":
        full_url = full_url.replace("https", "http")
        logger.info("get请求url为：{}".format(full_url))
        resp = requests.get(url=full_url, params=data, headers = full_header, verify = verify)
    else:
        resp = requests.post(full_url, json=data, headers=full_header, verify = verify)
    logger.info("响应状态码为：{}".format(resp.status_code))
    logger.info("响应数据为：{}".format(resp.json()))
    logger.info("************* HTTP请求结束 *************")
    return resp


def __handle_url(short_url: str):
    #把url拼接成一个完整的url
    if short_url.startswith("/"):
        new_url = conf.get("url", "base_url") + short_url
    else:
        new_url = conf.get("url", "base_url") + "/" + short_url
    return new_url


def __handle_header(header, token=None):
    global headers
    if header == 1:
        headers = {'App-ID': conf.get("UserInfo", "App-ID"), 'Content-Type': 'application/json'}
    elif header == 5:
        headers = {
                  'App-ID': conf.get("UserInfo", "App-ID"),
                  'Device-ID': conf.get("UserInfo", "Device-ID"),
                  'Distinct-Id': conf.get("UserInfo", "Distinct-Id"),
                  'Platform': conf.get("UserInfo", "Platform"),
                  'Version': conf.get("UserInfo", "Version"),
                  'Content-Type': 'application/json',
                }
    if token:
        headers["Access-Token"] = token
    return headers



if __name__ == '__main__':
    data = json.loads(conf.get("UserInfo", "login_account"))
    url = "/jdx-qa-service/app/authentication/captcha/register/login"
    resp = send_requests("post", url = url, data=data, header=5)
    resp_dict = resp.json()
    print(type(resp.json()))
    refresh_token = jsonpath.jsonpath(resp_dict, "$..token")
    print(refresh_token)