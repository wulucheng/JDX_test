"""
项目的名称: 质检接口测试
文件的名称： 06_IOS_USB_Check 
文件时间： 2021-01-28 13:55
"""


# 没在计划中，先不做

"""
接口URL：https://sjapi.aihuishou.com/jdx-qa-service/app/inspection/report/receive/inspection-app/v2
方法：POST
Headers: 
        App-ID：jdx470738       (数据库写死的，和账号绑定)
        Device-ID: 28FA6046-467C-4AC3-980D-F6846E3627AF   #应该是手机的ID
        Distinct-Id: BEAEA120-0387-4D18-BEBF-D565D945FAAE  #应该是手机的唯一码
        Platform： ios   #请求的平台
        Version: 4.0.3   #机大侠App的版本
        Access-Token: f055e3aa196dd32c0f7e9d281b2af393 #取自登陆接口返回json中的token

入参:
{"productName":"苹果 iPhone 11","hardwareOriginalModel":{"iyjd":"A1C5D92A064B3147B83135344E000000","q2":"A2223","i2":"MWN62","iyjl":"1057","zf":"G8R9495DC3MJYW58U","iyje":"18","a3":"false","j2":"CH\/A","iyjm":"false","iyjf":"\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/","b3":"L","iyjn":"true","a":"iPhone","b":"iPhone","c":"iPhone 11","c3":"659965320265774","iyjg":"\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/","d":"iPhone12,1","e":"13.5.1","f":"","iyjo":"Pass","g":"Activated","h":"1","d3":"00008030-0002583C267A802E","i":"MWN62","m2":"F3Y95210FNEL73WC","iyjh":"99","j":"CH\/A","k":"356338109586424","iyja":"BBInfoAvailable","l":"356338109836274","pingmu":"","iyjp":"true","m":"F3Y95210FNEL73WC","n":"e8:fb:e9:45:b8:84","n2":"E8FBE945B884","iyji":"64000000000","o":"e8:fb:e9:59:33:af","deviceId":"JDX-A21UK00003","p":"e8:fb:e9:4d:f2:97","w2":"","q":"A2223","iyjb":"false","iyjq":"64000000000","r":"64.0 GB","aa2":"DNPZX7H1N740","zf2":"G8R9495DC3MJYW58U","s":"false","o2":"E8FBE95933AF","t":"30","iyjj":"","u":"3200","v":"3092","w":"F8Y950425JPM6YMAX","iyjc":"D12DC5A1","x":"3","p2":"E8FBE94DF297","y":"","zb2":"DNL94724U2FK91P3R","boxVersion":"V3.2.4_RELEASE","iyjk":"FXC9327TTFCKQ5R69+18106130598167047098754193","y2":"","zb":"DNL94724U2FK91P3R","aa":"DNPZX7H1N740"},"properties":[{"isSkuProperty":true,"propertyValueName":"大陆国行（苹果系统型号M开头）","isPreferredValue":true,"propertyTypeName":"基本问题","propertyValueId":2014,"propertyType":1,"propertyNameId":314,"propertyName":"购买渠道","propertyNameOrder":1052},{"isSkuProperty":true,"propertyValueName":"64G","isPreferredValue":false,"propertyTypeName":"基本问题","propertyValueId":2023,"propertyType":1,"propertyNameId":315,"propertyName":"存储容量","propertyNameOrder":1051},{"isSkuProperty":false,"propertyValueName":"充电正常","isPreferredValue":true,"propertyTypeName":"功能使用问题","propertyValueId":2106,"propertyType":2,"propertyNameId":346,"propertyName":"充电功能 ","propertyNameOrder":2027},{"isSkuProperty":false,"propertyValueName":"正常连接电脑","isPreferredValue":true,"propertyTypeName":"功能使用问题","propertyValueId":9507,"propertyType":2,"propertyNameId":1359,"propertyName":"数据连接功能","propertyNameOrder":2047},{"isSkuProperty":true,"propertyValueName":"A2223","isPreferredValue":false,"propertyTypeName":"基本问题","propertyValueId":11016,"propertyType":1,"propertyNameId":1102,"propertyName":"小型号","propertyNameOrder":1015}],"deviceId":"JDX-A21UK00003","productId":32290,"boxVersion":"V3.2.4_RELEASE"}

出参：
{
    "code": 200,
    "data": {
        "boxVersion": "V3.2.4_RELEASE",
        "deviceId": "JDX-A21UK00003",
        "errorDes": "1项异常:可能更换过液晶显示屏",
        "errorList": [
            {
                "errorName": "可能更换过液晶显示屏"
            }
        ],
        "functionDetailApiModelList": [
            {
                "isSkuProperty": true,
                "propertyName": "购买渠道",
                "propertyNameId": 314,
                "propertyValueId": 2014,
                "propertyValueName": "大陆国行（苹果系统型号M开头）",
                "type": 2
            },
            {
                "isSkuProperty": true,
                "propertyName": "存储容量",
                "propertyNameId": 315,
                "propertyValueId": 2023,
                "propertyValueName": "64G",
                "type": 2
            },
            {
                "isSkuProperty": false,
                "propertyName": "维修情况",
                "propertyNameId": 332,
                "propertyValueId": 2965,
                "propertyValueName": "屏幕维修",
                "type": 2
            },
            {
                "isSkuProperty": false,
                "propertyName": "充电功能 ",
                "propertyNameId": 346,
                "propertyValueId": 2106,
                "propertyValueName": "充电正常",
                "type": 2
            },
            {
                "isSkuProperty": true,
                "propertyName": "机身颜色",
                "propertyNameId": 456,
                "propertyValueId": 2959,
                "propertyValueName": "绿色",
                "type": 2
            },
            {
                "isSkuProperty": true,
                "propertyName": "小型号",
                "propertyNameId": 1102,
                "propertyValueId": 11016,
                "propertyValueName": "A2223",
                "type": 2
            },
            {
                "isSkuProperty": false,
                "propertyName": "数据连接功能",
                "propertyNameId": 1359,
                "propertyValueId": 9507,
                "propertyValueName": "正常连接电脑",
                "type": 2
            },
            {
                "isSkuProperty": false,
                "propertyName": "是否可恢复出厂设置",
                "propertyNameId": 1364,
                "propertyValueId": 9625,
                "propertyValueName": "已激活，可还原",
                "type": 2
            }
        ],
        "hardwareDetailFormatApiModel": {
            "areaString": "成都富士康",
            "batteryLife": "100%",
            "breakState": 0,
            "crashLogResponseModel": {
                "crashCount": 0,
                "crashLogs": [],
                "resetCount": 1,
                "udid": "00008030-0002583C267A802E"
            },
            "errorDes": "1项异常",
            "iclound": 0,
            "imei": "356338109586424",
            "insureDate": "2021年06月07日 / 剩余130天",
            "iosVersion": "13.5.1",
            "itemList": [
                {
                    "errorName": "可能更换过液晶显示屏",
                    "isNormal": false,
                    "name": "液晶显示器",
                    "readValue": "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
                },
                {
                    "actualValue": "iPhone11",
                    "isNormal": true,
                    "name": "设备型号",
                    "readValue": "iPhone11"
                },
                {
                    "isNormal": true,
                    "name": "设备颜色",
                    "readValue": "绿色"
                },
                {
                    "actualValue": "64GB",
                    "isNormal": true,
                    "name": "硬盘容量",
                    "readValue": "64GB"
                },
                {
                    "actualValue": "MWN62",
                    "isNormal": true,
                    "name": "销售型号",
                    "readValue": "MWN62"
                },
                {
                    "actualValue": "CH/A 中国",
                    "isNormal": true,
                    "name": "销售地区",
                    "readValue": "CH/A 中国"
                },
                {
                    "actualValue": "A2223",
                    "isNormal": true,
                    "name": "监管型号",
                    "readValue": "A2223"
                },
                {
                    "actualValue": "e8:fb:e9:45:b8:84",
                    "isNormal": true,
                    "name": "蓝牙地址",
                    "readValue": "e8:fb:e9:45:b8:84"
                },
                {
                    "actualValue": "e8:fb:e9:4d:f2:97",
                    "isNormal": true,
                    "name": "蜂窝地址",
                    "readValue": "e8:fb:e9:4d:f2:97"
                },
                {
                    "actualValue": "e8:fb:e9:59:33:af",
                    "isNormal": true,
                    "name": "WiFi地址",
                    "readValue": "e8:fb:e9:59:33:af"
                },
                {
                    "actualValue": "DNPZX7H1N740",
                    "isNormal": true,
                    "name": "整机序列号",
                    "readValue": "DNPZX7H1N740"
                },
                {
                    "actualValue": "F3Y95210FNEL73WC",
                    "isNormal": true,
                    "name": "主板序列号",
                    "readValue": "F3Y95210FNEL73WC"
                },
                {
                    "isNormal": true,
                    "name": "电池序列号",
                    "readValue": "F8Y950425JPM6YMAX"
                },
                {
                    "actualValue": "G8R9495DC3MJYW58U",
                    "isNormal": true,
                    "name": "前置摄像头",
                    "readValue": "G8R9495DC3MJYW58U"
                },
                {
                    "actualValue": "DNL94724U2FK91P3R",
                    "isNormal": true,
                    "name": "后置摄像头",
                    "readValue": "DNL94724U2FK91P3R"
                },
                {
                    "isNormal": true,
                    "name": "基带",
                    "readValue": "BBInfoAvailable"
                }
            ],
            "machineNo": "DNPZX7H1N740",
            "produceDate": "2019年12月29日",
            "quinary": 1,
            "rechargeNumber": "30",
            "saleAreaString": "CH/A 中国",
            "saleTypeString": "零售机",
            "sequence": 1,
            "wifiModuleString": "低温WIFI"
        },
        "imeis": [
            "356338109586424",
            "356338109836274"
        ],
        "mainTitle": "苹果 iPhone 11 64GB 绿色",
        "productId": 32290,
        "productName": "苹果 iPhone 11",
        "reportNo": "R1354670687394045952",
        "skuName": "苹果 iPhone 11 64GB 绿色 A2223",
        "sn": "DNPZX7H1N740"
    },
    "resultMessage": ""
}

"""