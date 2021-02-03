"""
项目的名称: 质检接口测试
文件的名称： 03_Android_USB_Check 
文件时间： 2021-01-28 10:02
"""

"""
URL：https://sjapi.aihuishou.com/jdx-qa-service/app/inspection/report/receive/hardware/android
方法：POST
Headers：
    Access-Token：55621bf457ea55f00525dc000a13e208   #来源于登陆接口最后获取的accessToken
    App-ID： jdx470738  #数据库写死的，和账号绑定

入参：
{
	"imeiOrSn": "E6E4C20602016564",
	"deviceInfoBrand": "HUAWEI"
}

出参：   <会有两种出参，根据不同型号的机器返回结果不同>
①. {"code": 500000009,"resultMessage": "暂不支持该型号检测"}
②. 
{
    "code": 200,
    "data": {
        "functionProperties": [
            {
                "propertyName": "开机情况",
                "propertyNameId": 316,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 0,
                        "propertyValueId": 2026,
                        "propertyValueName": "正常开机"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 1,
                        "propertyValueId": 9630,
                        "propertyValueName": "有开机密码"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 2,
                        "propertyValueId": 6870,
                        "propertyValueName": "不可进入桌面，开机时不断重启或开机时卡死"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 3,
                        "propertyValueId": 2027,
                        "propertyValueName": "无法开机"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 4,
                        "propertyValueId": 12469,
                        "propertyValueName": "可进入桌面，进入后间歇性自动重启"
                    }
                ]
            },
            {
                "propertyName": "通话功能",
                "propertyNameId": 325,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 1,
                        "propertyValueId": 2045,
                        "propertyValueName": "通话功能正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 4,
                        "propertyValueId": 6941,
                        "propertyValueName": "声音功能不正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 5,
                        "propertyValueId": 2047,
                        "propertyValueName": "不读卡/不通话/无信号/无基带"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 13,
                        "propertyValueId": 12541,
                        "propertyValueName": "信号弱/信号不稳定"
                    }
                ]
            },
            {
                "propertyName": "指纹功能",
                "propertyNameId": 344,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 1,
                        "propertyValueId": 2102,
                        "propertyValueName": "指纹功能正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 4,
                        "propertyValueId": 2103,
                        "propertyValueName": "指纹无法完全录入和解锁"
                    }
                ]
            },
            {
                "propertyName": "拍摄功能",
                "propertyNameId": 345,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 0,
                        "propertyValueId": 2104,
                        "propertyValueName": "拍照摄像正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 2,
                        "propertyValueId": 10201,
                        "propertyValueName": "后摄像头拍照有斑"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 3,
                        "propertyValueId": 6942,
                        "propertyValueName": "画面异常（抖动/模糊/不对焦/颠倒/分层）"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 4,
                        "propertyValueId": 2105,
                        "propertyValueName": "拍照无法开关/报错/全黑/闪光灯坏"
                    }
                ]
            },
            {
                "propertyName": "充电功能 ",
                "propertyNameId": 346,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 0,
                        "propertyValueId": 2106,
                        "propertyValueName": "充电正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 3,
                        "propertyValueId": 2107,
                        "propertyValueName": "充电无反应/充电孔接触不良"
                    }
                ]
            },
            {
                "propertyName": "无线功能 ",
                "propertyNameId": 347,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 0,
                        "propertyValueId": 2108,
                        "propertyValueName": "无线正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 2,
                        "propertyValueId": 2109,
                        "propertyValueName": "无线无法打开/无法连接"
                    }
                ]
            },
            {
                "propertyName": "触摸功能",
                "propertyNameId": 580,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 0,
                        "propertyValueId": 3168,
                        "propertyValueName": "触摸功能正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 3,
                        "propertyValueId": 3169,
                        "propertyValueName": "触摸失灵/延迟"
                    }
                ]
            },
            {
                "propertyName": "账号",
                "propertyNameId": 592,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 0,
                        "propertyValueId": 3222,
                        "propertyValueName": "账号已注销"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 3,
                        "propertyValueId": 3223,
                        "propertyValueName": "账号无法注销"
                    }
                ]
            },
            {
                "propertyName": "面容识别功能",
                "propertyNameId": 1135,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 1,
                        "propertyValueId": 5300,
                        "propertyValueName": "面容识别功能正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 4,
                        "propertyValueId": 5299,
                        "propertyValueName": "面容无法录入和识别"
                    }
                ]
            },
            {
                "propertyName": "屏幕传感器功能",
                "propertyNameId": 1268,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 0,
                        "propertyValueId": 6947,
                        "propertyValueName": "光线、距离感应正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 2,
                        "propertyValueId": 6948,
                        "propertyValueName": "光线/距离感应不正常"
                    }
                ]
            },
            {
                "propertyName": "震动功能",
                "propertyNameId": 1269,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 1,
                        "propertyValueId": 6949,
                        "propertyValueName": "振动正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 3,
                        "propertyValueId": 6950,
                        "propertyValueName": "振动不正常"
                    }
                ]
            },
            {
                "propertyName": "侧键",
                "propertyNameId": 1669,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 1,
                        "propertyValueId": 11210,
                        "propertyValueName": "侧键正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 3,
                        "propertyValueId": 11212,
                        "propertyValueName": "侧键按压无反馈或失灵"
                    }
                ]
            },
            {
                "propertyName": "售后案例情况",
                "propertyNameId": 1899,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 1,
                        "propertyValueId": 12604,
                        "propertyValueName": "无售后维修案例"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 2,
                        "propertyValueId": 12603,
                        "propertyValueName": "有售后维修案例"
                    }
                ]
            }
        ],
        "inspectionReportNo": "R1354612678865305600",
        "inspectionSource": 1,
        "isInspectionApp": false,
        "mainTitle": "华为 nova 7（5G版） 8G+128G",
        "price": 2504,
        "productId": 34754,
        "qualityModel": {
            "items": [
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 2800,
                    "itemName": "屏幕显示",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 28001,
                            "itemValueName": "显示完美",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 28002,
                            "itemValueName": "显示色差",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 28003,
                            "itemValueName": "显示色斑",
                            "order": 3
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 28004,
                            "itemValueName": "显示透图",
                            "order": 4
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 28005,
                            "itemValueName": "显示黑色屏幕",
                            "order": 5
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 28006,
                            "itemValueName": "显示异常",
                            "order": 6
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 28007,
                            "itemValueName": "不显示/全花屏",
                            "order": 7
                        }
                    ],
                    "order": 1
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 2900,
                    "itemName": "屏幕外观",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 29001,
                            "itemValueName": "完美无划痕",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 29002,
                            "itemValueName": "屏细微划痕",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 29003,
                            "itemValueName": "屏幕划伤",
                            "order": 3
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 29004,
                            "itemValueName": "屏有碎裂/缺角",
                            "order": 4
                        }
                    ],
                    "order": 2
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 3000,
                    "itemName": "边框背板",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 30001,
                            "itemValueName": "外壳完美",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 30002,
                            "itemValueName": "外壳划痕/小磕",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 30003,
                            "itemValueName": "外壳磕碰掉漆",
                            "order": 3
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 30004,
                            "itemValueName": "外壳缺失/裂缝/刻字",
                            "order": 4
                        }
                    ],
                    "order": 3
                },
                {
                    "isHidden": 0,
                    "itemGroup": 1,
                    "itemId": 2600,
                    "itemName": "主板维修",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 26001,
                            "itemValueName": "无维修情况",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 26002,
                            "itemValueName": "主板小修",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 26003,
                            "itemValueName": "主板维修/扩容",
                            "order": 3
                        }
                    ],
                    "order": 4
                },
                {
                    "isHidden": 0,
                    "itemGroup": 1,
                    "itemId": 2700,
                    "itemName": "屏幕维修",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 27001,
                            "itemValueName": "无维修情况",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 27002,
                            "itemValueName": "外屏维修",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 27003,
                            "itemValueName": "屏幕维修",
                            "order": 3
                        }
                    ],
                    "order": 5
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 3100,
                    "itemName": "受潮情况",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 31001,
                            "itemValueName": "机身无进水",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 31002,
                            "itemValueName": "机身进水/受潮",
                            "order": 2
                        }
                    ],
                    "order": 6
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 3200,
                    "itemName": "是否弯曲",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 32001,
                            "itemValueName": "机身无弯曲",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 32002,
                            "itemValueName": "机身弯曲",
                            "order": 2
                        }
                    ],
                    "order": 7
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 3300,
                    "itemName": "零件维修",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 33001,
                            "itemValueName": "电池/摄像头/外壳/尾插无维修",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 33002,
                            "itemValueName": "维修过电池/摄像头/外壳/充电(耳机)口",
                            "order": 2
                        }
                    ],
                    "order": 8
                }
            ],
            "properties": []
        },
        "reportNo": "R1354612166979870720",
        "skuName": "华为 nova 7（5G版） 8G+128G",
        "skuProperties": [
            {
                "propertyName": "购买渠道",
                "propertyNameId": 314,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 1,
                        "propertyValueId": 2014,
                        "propertyValueName": "大陆国行"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 5,
                        "propertyValueId": 3950,
                        "propertyValueName": "国行展示机"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 11,
                        "propertyValueId": 3445,
                        "propertyValueName": "非大陆国行"
                    }
                ]
            },
            {
                "propertyName": "机身颜色",
                "propertyNameId": 456,
                "propertyValues": [
                    {
                        "isBasic": 0,
                        "isSelected": 1,
                        "order": 999,
                        "propertyValueId": 3988,
                        "propertyValueName": "亮黑色"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 999,
                        "propertyValueId": 2935,
                        "propertyValueName": "紫色"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 999,
                        "propertyValueId": 2957,
                        "propertyValueName": "红色"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 999,
                        "propertyValueId": 2959,
                        "propertyValueName": "绿色"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 999,
                        "propertyValueId": 11467,
                        "propertyValueName": "7号色"
                    }
                ]
            },
            {
                "propertyName": "网络制式",
                "propertyNameId": 492,
                "propertyValues": [
                    {
                        "isBasic": 0,
                        "isSelected": 1,
                        "order": 1,
                        "propertyValueId": 3084,
                        "propertyValueName": "全网通"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 2,
                        "propertyValueId": 12114,
                        "propertyValueName": "运营商版全网通"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 6,
                        "propertyValueId": 2567,
                        "propertyValueName": "移动版"
                    }
                ]
            },
            {
                "propertyName": "内存",
                "propertyNameId": 806,
                "propertyValues": [
                    {
                        "isBasic": 0,
                        "isSelected": 1,
                        "order": 12,
                        "propertyValueId": 5032,
                        "propertyValueName": "8G+128G"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 11,
                        "propertyValueId": 5835,
                        "propertyValueName": "8G+256G"
                    }
                ]
            }
        ],
        "sn": "E6E4C20602016564",
        "suggestRecyclePrice": 2204,
        "viceTitle": "大陆国行 | 亮黑色 | 全网通"
    },
    "resultMessage": ""
}


"""