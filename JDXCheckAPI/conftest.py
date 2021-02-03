"""
项目的名称: main.py
文件的名称： conftest 
文件时间： 2021-01-29 9:29
"""


import pytest
import json
import jsonpath

from Common.handle_config import conf
from Common.handle_request import send_requests
from Common.my_logger import logger


@pytest.fixture(scope="class")
def login_accessToken():
    #登陆获取refreshToken和token
    logger.info("前置条件：开始运行！")
    login_data = json.loads(conf.get("UserInfo", "login_account"))
    login_url = "jdx-account-service/app/authentication/captcha/register/login"
    resp = send_requests("post", url = login_url, data=login_data, header=5)
    resp_dict = resp.json()
    logger.info("前置条件：登陆成功！响应结果为{}".format(resp_dict))

    #使用token获取accessToken
    refresh_token = jsonpath.jsonpath(resp_dict, "$..refreshToken")[0]
    token = jsonpath.jsonpath(resp_dict, "$..token")[0]
    token_data = {"refreshToken":refresh_token}
    token_url = "sj-api/auth/refresh-token"
    token_resp = send_requests("post", url=token_url, header=5, data=token_data,token=token)
    accessToken = jsonpath.jsonpath(token_resp.json(), "$..accessToken")[0]
    logger.info("前置条件：获取accessToken成功！它的值是：{}".format(accessToken))
    yield accessToken


if __name__ == '__main__':
    pass