"""
项目的名称: main.py
文件的名称： test_02_Manual_Inquiry 
文件时间： 2021-01-29 16:40
"""


import pytest

from TestData.data_02_manual_inquiry import data_manual_inquiry
from Common.handle_request import send_requests
from Common.my_logger import logger


class TestManualInquiry:

    @pytest.mark.usefixtures("login_accessToken")
    @pytest.mark.parametrize("case", data_manual_inquiry)
    def test_manual_inquiry(self, login_accessToken, case):
        logger.info("===================== 开始执行测试用例 ===================")
        logger.info("该case的值是：{}".format(case))
        inquiry_url = "jdx-qa-service/" + case["url"]
        param_data = {"productId": case["param"]}
        resp = send_requests(method="get", url=inquiry_url, header=1, data=param_data, token=login_accessToken)
        print(case["param"])
        print("响应的结果是：{}".format(resp.json()))
        logger.info("===================== 测试用例执行结束 ===================")

