"""
项目的名称: 质检接口测试
文件的名称： 05_Receive_Report_from_Asistant 
文件时间： 2021-01-28 13:40
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
        
        
入参：
{"appId": "jdx220201","sn": "E6E4C20602016564","uniqueNo": "981e1f01-d8f6-308c-a937-84e599a2ab43","appCodes": [{"value": "1", "code": "Compass"},{"value": "1","code": "Vibrator"},{"value": "1","code": "GSensor"},{"value": "1","code": "WIFI"},{"value": "2","code": "Bluetooth"},{"value": "2","code": "PSensor"},{"value": "1","code": "LightSensorStatus"},{"value": "1","code": "FlashLightManual"},{"value": "1","code": "TouchScreen"},{"value": "1","code": "microphone"},{"value": "1","code": "speaker"},{"value": "1","code": "earpiece"},{"value": "2","code": "button"},{"value": "1","code": "FrontCamera"},{"value": "1","code": "MainCamera"},{"value": "3","code": "ScreenDisplay"},{"value": "1","code": "TouchId"},{"value": "1","code": "USBCharge"},{"value": "1","code": "Telephony.Status"},{"value": "true","code": "DeviceInfo.canPowerOn"},{"value": "HUAWEI","code": "DeviceInfo_Brand"},{"value": "JEF-AN00","code": "DeviceInfo_Model"},{"value": "8G","code": "DeviceInfo_RAM_G"},{"value": "7871758336","code": "DeviceInfo.RAM"},{"value": "128G","code": "DeviceInfo_StorageCapacity_G"},{"value": "119789424640","code": "Storage.IntStorageCapacity"},{"value": "2400x1080","code": "DeviceInfo_ScreenResolution"},{"value": "1","code": "Deviceinfo_TouchidStatus"},{"value": "kirin985","code": "Deviceinfo_CPUModel"},{"value": "2.6GHz","code": "Deviceinfo_CPUFrequent"},{"value": "6400万","code": "Deviceinfo_CameraResolution"},{"value": "6400万","code": "Deviceinfo_Camera_Main"},{"value": "3200万","code": "Deviceinfo_Camera_Front"}]}

出参：
{
    "code": 200,
    "data": {
        "brandId": 9,
        "brandName": "华为 ",
        "categoryId": 1,
        "categoryName": "手机",
        "createTime": "2021-01-28 10:08:02",
        "errorDes": "4项异常:屏幕显示、蓝牙、音量键、距离感应器",
        "errorList": [
            {
                "errorName": "屏幕显示"
            },
            {
                "errorName": "蓝牙"
            },
            {
                "errorName": "音量键"
            },
            {
                "errorName": "距离感应器"
            }
        ],
        "functionDetailApiModelList": [
            {
                "isSkuProperty": false,
                "propertyName": "开机情况",
                "propertyNameId": 316,
                "propertyValueId": 2026,
                "propertyValueName": "正常开机",
                "type": 3
            },
            {
                "isSkuProperty": false,
                "propertyName": "通话功能",
                "propertyNameId": 325,
                "propertyValueId": 2045,
                "propertyValueName": "通话功能正常",
                "type": 3
            },
            {
                "isSkuProperty": false,
                "propertyName": "指纹功能",
                "propertyNameId": 344,
                "propertyValueId": 2102,
                "propertyValueName": "指纹功能正常",
                "type": 3
            },
            {
                "isSkuProperty": false,
                "propertyName": "拍摄功能",
                "propertyNameId": 345,
                "propertyValueId": 2104,
                "propertyValueName": "拍照摄像正常",
                "type": 3
            },
            {
                "isSkuProperty": false,
                "propertyName": "充电功能 ",
                "propertyNameId": 346,
                "propertyValueId": 2106,
                "propertyValueName": "充电正常",
                "type": 3
            },
            {
                "isSkuProperty": false,
                "propertyName": "无线功能 ",
                "propertyNameId": 347,
                "propertyValueId": 2109,
                "propertyValueName": "无线无法打开/无法连接",
                "type": 3
            },
            {
                "isSkuProperty": false,
                "propertyName": "屏幕显示",
                "propertyNameId": 350,
                "propertyValueId": 2475,
                "propertyValueName": "显示异常（漏液/错乱/闪屏/屏生线）",
                "type": 3
            },
            {
                "isSkuProperty": false,
                "propertyName": "触摸功能",
                "propertyNameId": 580,
                "propertyValueId": 3168,
                "propertyValueName": "触摸功能正常",
                "type": 3
            },
            {
                "isSkuProperty": true,
                "propertyName": "内存",
                "propertyNameId": 806,
                "propertyValueId": 5032,
                "propertyValueName": "8G+128G",
                "type": 3
            },
            {
                "isSkuProperty": false,
                "propertyName": "屏幕传感器功能",
                "propertyNameId": 1268,
                "propertyValueId": 6948,
                "propertyValueName": "光线/距离感应不正常",
                "type": 3
            },
            {
                "isSkuProperty": false,
                "propertyName": "震动功能",
                "propertyNameId": 1269,
                "propertyValueId": 6949,
                "propertyValueName": "振动正常",
                "type": 3
            }
        ],
        "inspectionAppDetailApiModelList": [
            {
                "code": "Compass",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "指南针",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "Vibrator",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "震动功能",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "GSensor",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "重力感应器",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "WIFI",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "Wi-Fi",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "Bluetooth",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 1,
                "name": "蓝牙",
                "reportNo": "R1354612166979870720",
                "value": "2"
            },
            {
                "code": "PSensor",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 1,
                "name": "距离感应器",
                "reportNo": "R1354612166979870720",
                "value": "2"
            },
            {
                "code": "LightSensorStatus",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "光线感应器",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "FlashLightManual",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "闪光灯",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "TouchScreen",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "触摸功能",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "microphone",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "麦克风",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "speaker",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "扬声器",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "earpiece",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "听筒",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "button",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 1,
                "name": "音量键",
                "reportNo": "R1354612166979870720",
                "value": "2"
            },
            {
                "code": "FrontCamera",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "前置摄像头",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "MainCamera",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "后置摄像头",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "ScreenDisplay",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 1,
                "name": "屏幕显示",
                "reportNo": "R1354612166979870720",
                "value": "3"
            },
            {
                "code": "TouchId",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "指纹",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "USBCharge",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "充电功能",
                "reportNo": "R1354612166979870720",
                "value": "1"
            },
            {
                "code": "Telephony.Status",
                "createTime": "2021-01-28 13:43:20",
                "errorState": 0,
                "name": "通话功能",
                "reportNo": "R1354612166979870720",
                "value": "1"
            }
        ],
        "inspectionReportNo": "R1354665135091789824",
        "itemCode": "213859744207693824",
        "levelId": 445,
        "levelName": "I1",
        "productId": 34754,
        "productName": "华为 nova 7（5G版）",
        "reportNo": "R1354612166979870720",
        "skuId": 2060541,
        "skuName": "华为 nova 7（5G版） 8G+128G 亮黑色 大陆国行 全网通",
        "sn": "E6E4C20602016564",
        "uniqueNo": "981e1f01-d8f6-308c-a937-84e599a2ab43"
    },
    "resultMessage": ""
}

"""