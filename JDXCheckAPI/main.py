"""
项目的名称: 质检接口测试
文件的名称： test_data
文件时间： 2021-01-27 17:17
"""

import pytest


pytest.main(["-s", "-v", "TestCases\\test_02_Manual_Inquiry.py",
             "--alluredir=Outputs\\reports"])



"""
总计接口数：7

01.登陆的接口
{"captcha": "000000","mobile": "19128326083","appChannel": "jdx_00002"}

02.人工询价
{"param":36047,"name":"人工询价","type":"质检入参","url":"/app/inspection/report/create/report/default"}

03.android插线质检
{"param":{"deviceInfoBrand":"Xiaomi","imeiOrSn":"uolj6hi7ydojh6qo"},"name":"android插线质检","type":"质检入参","url":"/app/inspection/report/receive/hardware/android"}

04.OCR拍照询价
{"param":{"brandType":6,"imeiOrSn":"868744056604550"},"name":"OCR拍照询价","type":"质检入参","url":"/app/inspection/report/create/report/by-sku"}

05.接收助手
{"param":{"appCodes":[{"code":"Compass","value":"1"},{"code":"Vibrator","value":"1"},{"code":"GSensor","value":"1"},{"code":"WIFI","value":"1"},{"code":"Bluetooth","value":"1"},{"code":"PSensor","value":"1"},{"code":"LightSensorStatus","value":"1"},{"code":"FlashLightManual","value":"1"},{"code":"TouchScreen","value":"1"},{"code":"microphone","value":"1"},{"code":"speaker","value":"1"},{"code":"earpiece","value":"1"},{"code":"NetworkLock","value":"1"},{"code":"button","value":"1"},{"code":"VolumeMute","value":"1"},{"code":"3DTouch","value":"1"},{"code":"FrontCamera","value":"1"},{"code":"MainCamera","value":"1"},{"code":"ScreenDisplay","value":"1"},{"code":"FaceId","value":"1"},{"code":"USBCharge","value":"1"},{"code":"Telephony.Status","value":"1"},{"code":"DeviceInfo.DeviceColor","value":"1"},{"code":"DeviceInfo.DeviceEnclosureColor","value":"1"},{"code":"DeviceInfo.RAM","value":"3949592576"},{"code":"DeviceInfo_RAM_G","value":"4G"},{"code":"DeviceInfo_Model","value":"iPhone11,6"},{"code":"Storage.IntStorageCapacity","value":"63876222976"},{"code":"DeviceInfo_Brand","value":"iPhone"},{"code":"DeviceInfo_ScreenResolution","value":"2688x1242"},{"code":"DeviceInfo.canPowerOn","value":"true"},{"code":"Storage.DeviceInfo_StorageCapacity_G","value":"64G"},{"code":"DeviceInfo.RegionInfo","value":"KH"},{"code":"DeviceInfo.ModelOfA","value":"A2101"},{"code":"iCloudLock","value":"2"}],"appId":"jdx220201","imeis":["357289094038633","357289094093554"],"sn":"G6TXJ9PFKPH1","uniqueNo":"15C4029D-DFF9-4271-AE41-51AF4ACC487B"},"name":"接收助手","type":"质检入参","url":"/app/inspection/report/receive/inspection-app/v2"}

06.iOS插线
{"param":{"boxVersion":"V3.2.3_TEST","deviceId":"JDX-A21UL00652","hardwareOriginalModel":{"a":"iPhone","a3":false,"aa":"G0NZQ4FPN746","aa2":"G0NZQ4FPN746","b":"iPhone","b3":"L","c":"iPhone 11","c3":"1254843453833262","d":"iPhone12,1","d3":"00008030-000475460250802E","e":"14.3","g":"Activated","h":"1","i":"MWNE2","i2":"MWNE2","iyja":"BBNotReady","iyjb":false,"iyjc":"D13297A1","iyjd":"A197293A06464536A935323253000000","iyje":"18","iyjf":"C3F9465GB6FKV28AU+L332FE6522S7A3G12+C3F9447J9NKKWPPAZ+CX594560AF7N2N3AH+24E92PCAFF0SXD6N6F+C439446V8THLMD5AJ+WFF23A1","iyjg":"THLMD5AJ+WFF23A1","iyjh":21,"iyji":128000000000,"iyjj":"","iyjk":"FX993842PVKKQ5R6T+18011137562173050102777193","iyjl":1057,"iyjn":true,"iyjo":"Pass","iyjp":true,"iyjq":128000000000,"j":"CH/A","j2":"CH/A","k":"","l":"","m":"F3Y94712DBHL73YC","m2":"F3Y94712DBHL73YC","n":"b8:7b:c5:dc:98:10","n2":"B87BC5DC9810","o":"b8:7b:c5:cc:d8:45","o2":"B87BC5CCD845","p":"b8:7b:c5:dc:84:df","p2":"B87BC5DC84DF","pingmu":"","q":"A2223","q2":"A2223","r":"128.0 GB","s":false,"t":"500","u":2726,"v":3092,"w":"F8Y94461HV3M6YP73","w2":"","x":"3","y":"","y2":"","zb":"DNL93440ECPK91P93","zb2":"DNL93440ECPK91P93","zf":"G8R94538G1VJYW55S","zf2":"G8R94538G1VJYW55S"},"productId":32290,"productName":"苹果 iPhone 11","properties":[{"isSkuProperty":true,"propertyName":"购买渠道","propertyNameId":314,"propertyValueId":2014,"propertyValueName":"大陆国行（苹果系统型号M开头）"},{"isSkuProperty":true,"propertyName":"存储容量","propertyNameId":315,"propertyValueId":2024,"propertyValueName":"128G"},{"isSkuProperty":false,"propertyName":"开机情况","propertyNameId":316,"propertyValueId":2026,"propertyValueName":"正常开机"},{"isSkuProperty":false,"propertyName":"充电功能 ","propertyNameId":346,"propertyValueId":2106,"propertyValueName":"充电正常"},{"isSkuProperty":false,"propertyName":"数据连接功能","propertyNameId":1359,"propertyValueId":9507,"propertyValueName":"正常连接电脑"},{"isSkuProperty":true,"propertyName":"小型号","propertyNameId":1102,"propertyValueId":11016,"propertyValueName":"A2223"}]},"name":"iOS插线","type":"质检入参","url":"/app/inspection/report/receive/hardware"}

07.助手生成远端报告：
{"param":{"appId":"jdx220201","imeiMissReason":"无法自动获取或用户未填写","pricePropertyValues":[{"pricePropertyValueId":2067},{"pricePropertyValueId":3097},{"pricePropertyValueId":6872},{"pricePropertyValueId":2129},{"pricePropertyValueId":2134},{"pricePropertyValueId":3222},{"pricePropertyValueId":6982},{"pricePropertyValueId":11210},{"pricePropertyValueId":12604},{"pricePropertyValueId":2014},{"pricePropertyValueId":3084},{"pricePropertyValueId":4484},{"pricePropertyValueId":2026},{"pricePropertyValueId":6941},{"pricePropertyValueId":2104},{"pricePropertyValueId":2106},{"pricePropertyValueId":2108},{"pricePropertyValueId":2114},{"pricePropertyValueId":3168},{"pricePropertyValueId":2103},{"pricePropertyValueId":6947},{"pricePropertyValueId":6949}],"productId":29443},"name":"助手生成远端报告","type":"质检入参","url":"/app/inspection-app/report/create"}
"""
