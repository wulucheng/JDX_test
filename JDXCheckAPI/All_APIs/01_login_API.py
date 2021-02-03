"""
项目的名称: 质检接口测试
文件的名称： 01_login_API 
文件时间： 2021-01-28 9:29
"""

"""
登陆的账号密码：
19128326083/000000

============================= 登陆接口 =========================================

URL：https://sjapi.aihuishou.com/jdx-account-service/app/authentication/captcha/register/login

**************** 下面参数抓包自iPhoneX（编号107）手机 *****************
方法：POST
Headers: App-ID：jdx470738       (数据库写死的，和账号绑定)
        Device-ID: 28FA6046-467C-4AC3-980D-F6846E3627AF   #应该是手机的ID
        Distinct-Id: BEAEA120-0387-4D18-BEBF-D565D945FAAE  #应该是手机的唯一码
        Platform： ios   #请求的平台
        Version: 4.0.3   #机大侠App的版本

入参：
{"captcha": "000000","mobile": "19128326083","appChannel": "jdx_00002"}

出参：
{
    "code": 200,
    "data": {
        "optMerChantId": 147997,
        "refreshToken": "aa8280b1a60f3d523ada8d07c7c0c1c2",
        "refreshTokenExpiresIn": 2592000,
        "token": "f055e3aa196dd32c0f7e9d281b2af393",
        "tokenExpiresIn": 86400,
        "userId": 6
    },
    "resultMessage": ""
}


=========================== 获取accessToken的接口 ==============================================

URL：https://sjapi.aihuishou.com/sj-api/auth/refresh-token
方法：POST
Headers: App-ID：jdx470738       (数据库写死的，和账号绑定)
        Device-ID: 28FA6046-467C-4AC3-980D-F6846E3627AF   #应该是手机的ID
        Distinct-Id: BEAEA120-0387-4D18-BEBF-D565D945FAAE  #应该是手机的唯一码
        Platform： ios   #请求的平台
        Version: 4.0.3   #机大侠App的版本
        Access-Token: f055e3aa196dd32c0f7e9d281b2af393 #取自登陆接口返回json中的token

入参：
{"refreshToken": "aa8280b1a60f3d523ada8d07c7c0c1c2"} #取自登陆接口返回json中的refreshToken

出参：    #获取accessToken，后面请求的各种接口，都需要使用此Token
{
    "code": 200,
    "resultMessage": "",
    "data": {
        "merchantId": 147997,
        "merchantName": "梁荣寅",
        "accessToken": "55621bf457ea55f00525dc000a13e208",
        "tokenExpiresIn": 86400,
        "refreshToken": "aa8280b1a60f3d523ada8d07c7c0c1c2",
        "refreshTokenExpiresIn": 2592000,
        "newMerchant": 0
    }
}

"""