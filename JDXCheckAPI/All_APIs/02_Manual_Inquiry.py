"""
项目的名称: 质检接口测试
文件的名称： 02_Manual_Inquiry 
文件时间： 2021-01-28 9:51
"""

"""
接口URL：http://sjapi.aihuishou.com/jdx-qa-service/app/inspection/report/create/report/default

请求方法：POST
请求参数：
    productId：34701
Headers：
    Access-Token：55621bf457ea55f00525dc000a13e208   #来源于登陆接口最后获取的accessToken
    App-ID： jdx470738  #数据库写死的，和账号绑定
    
出参：
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
                "propertyName": "指南针功能",
                "propertyNameId": 529,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 0,
                        "propertyValueId": 2808,
                        "propertyValueName": "指南针功能正常"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 2,
                        "propertyValueId": 2809,
                        "propertyValueName": "指南针功能不正常"
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
                "propertyName": "数据连接功能",
                "propertyNameId": 1359,
                "propertyValues": [
                    {
                        "isBasic": 1,
                        "isSelected": 1,
                        "order": 0,
                        "propertyValueId": 9507,
                        "propertyValueName": "正常连接电脑"
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
        "inspectionReportNo": "R1354602098410504192",
        "inspectionSource": 4,
        "isInspectionApp": false,
        "mainTitle": "苹果 iPhone SE 2 256G",
        "price": 2485,
        "productId": 34701,
        "qualityModel": {
            "items": [
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 1900,
                    "itemName": "屏幕显示",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 19001,
                            "itemValueName": "显示完美",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 19002,
                            "itemValueName": "显示色差",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 19003,
                            "itemValueName": "显示色斑",
                            "order": 3
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 19005,
                            "itemValueName": "显示黑色屏幕",
                            "order": 5
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 19006,
                            "itemValueName": "显示异常",
                            "order": 6
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 19007,
                            "itemValueName": "不显示/全花屏",
                            "order": 7
                        }
                    ],
                    "order": 1
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 2000,
                    "itemName": "屏幕外观",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 20001,
                            "itemValueName": "完美无划痕",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 20002,
                            "itemValueName": "屏细微划痕",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 20003,
                            "itemValueName": "屏幕划伤",
                            "order": 3
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 20004,
                            "itemValueName": "屏有碎裂/缺角",
                            "order": 4
                        }
                    ],
                    "order": 2
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 2100,
                    "itemName": "边框背板",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 21001,
                            "itemValueName": "外壳完美",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 21002,
                            "itemValueName": "外壳划痕/小磕",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 21003,
                            "itemValueName": "外壳磕碰掉漆",
                            "order": 3
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 21004,
                            "itemValueName": "外壳缺失/裂缝/刻字",
                            "order": 4
                        }
                    ],
                    "order": 3
                },
                {
                    "isHidden": 0,
                    "itemGroup": 1,
                    "itemId": 1700,
                    "itemName": "主板维修",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 17001,
                            "itemValueName": "无维修情况",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 17002,
                            "itemValueName": "主板小修",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 17003,
                            "itemValueName": "主板维修/扩容",
                            "order": 3
                        }
                    ],
                    "order": 4
                },
                {
                    "isHidden": 0,
                    "itemGroup": 1,
                    "itemId": 1800,
                    "itemName": "屏幕维修",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 18001,
                            "itemValueName": "无维修情况",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 18002,
                            "itemValueName": "外屏维修",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 18003,
                            "itemValueName": "屏幕维修",
                            "order": 3
                        }
                    ],
                    "order": 5
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 2200,
                    "itemName": "受潮情况",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 22001,
                            "itemValueName": "机身无进水",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 22002,
                            "itemValueName": "机身进水/受潮",
                            "order": 2
                        }
                    ],
                    "order": 6
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 2300,
                    "itemName": "是否弯曲",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 23001,
                            "itemValueName": "机身无弯曲",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 23002,
                            "itemValueName": "机身弯曲",
                            "order": 1
                        }
                    ],
                    "order": 7
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 2400,
                    "itemName": "零件维修",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 24001,
                            "itemValueName": "电池/摄像头/外壳/尾插无维修",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 24002,
                            "itemValueName": "维修过电池/摄像头/外壳/充电(耳机)口",
                            "order": 2
                        }
                    ],
                    "order": 8
                },
                {
                    "isHidden": 0,
                    "itemGroup": 0,
                    "itemId": 2500,
                    "itemName": "可否还原",
                    "itemValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "itemValueId": 25001,
                            "itemValueName": "已激活可还原",
                            "order": 1
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 25002,
                            "itemValueName": "已激活不可还原",
                            "order": 2
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "itemValueId": 25003,
                            "itemValueName": "无法还原/无法激活",
                            "order": 3
                        }
                    ],
                    "order": 9
                }
            ],
            "properties": [
                {
                    "propertyName": "账  号",
                    "propertyNameId": 343,
                    "propertyValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "order": 0,
                            "propertyValueId": 2100,
                            "propertyValueName": "iCloud已注销  "
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "order": 1,
                            "propertyValueId": 2101,
                            "propertyValueName": "iCloud无法注销  "
                        }
                    ]
                },
                {
                    "propertyName": "实体按键功能",
                    "propertyNameId": 1267,
                    "propertyValues": [
                        {
                            "isBasic": 1,
                            "isSelected": 1,
                            "order": 0,
                            "propertyValueId": 6944,
                            "propertyValueName": "HOME按鍵正常"
                        },
                        {
                            "isBasic": 0,
                            "isSelected": 0,
                            "order": 2,
                            "propertyValueId": 6946,
                            "propertyValueName": "HOME键按压无反馈或失灵"
                        }
                    ]
                }
            ]
        },
        "reportNo": "R1354602099198971904",
        "skuName": "苹果 iPhone SE 2 256G",
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
                        "order": 2,
                        "propertyValueId": 2984,
                        "propertyValueName": "国行官换机"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 3,
                        "propertyValueId": 7050,
                        "propertyValueName": "国行官修机"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 4,
                        "propertyValueId": 2015,
                        "propertyValueName": "港澳台版"
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
                        "order": 6,
                        "propertyValueId": 11245,
                        "propertyValueName": "美版无锁"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 7,
                        "propertyValueId": 11246,
                        "propertyValueName": "日版无锁"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 8,
                        "propertyValueId": 11247,
                        "propertyValueName": "欧版无锁"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 9,
                        "propertyValueId": 11248,
                        "propertyValueName": "韩版无锁"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 12,
                        "propertyValueId": 2794,
                        "propertyValueName": "其他国家-无锁（含零售/官修官换/展示机）"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 13,
                        "propertyValueId": 2019,
                        "propertyValueName": "非国行有锁"
                    }
                ]
            },
            {
                "propertyName": "存储容量",
                "propertyNameId": 315,
                "propertyValues": [
                    {
                        "isBasic": 0,
                        "isSelected": 1,
                        "order": 2,
                        "propertyValueId": 3987,
                        "propertyValueName": "256G"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 3,
                        "propertyValueId": 2024,
                        "propertyValueName": "128G"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 4,
                        "propertyValueId": 2023,
                        "propertyValueName": "64G"
                    }
                ]
            },
            {
                "propertyName": "苹果保修期时长",
                "propertyNameId": 333,
                "propertyValues": [
                    {
                        "isBasic": 0,
                        "isSelected": 1,
                        "order": 1,
                        "propertyValueId": 12479,
                        "propertyValueName": "保修≥ 330天"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 2,
                        "propertyValueId": 12478,
                        "propertyValueName": "保修250-330天"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 3,
                        "propertyValueId": 12477,
                        "propertyValueName": "保修190-250天"
                    },
                    {
                        "isBasic": 1,
                        "isSelected": 0,
                        "order": 4,
                        "propertyValueId": 2072,
                        "propertyValueName": "保修110-190天"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 5,
                        "propertyValueId": 12475,
                        "propertyValueName": "保修30-110天"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 6,
                        "propertyValueId": 2075,
                        "propertyValueName": "保修＜30天"
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
                        "propertyValueId": 2957,
                        "propertyValueName": "红色"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 999,
                        "propertyValueId": 2453,
                        "propertyValueName": "白色"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 999,
                        "propertyValueId": 2454,
                        "propertyValueName": "黑色"
                    }
                ]
            },
            {
                "propertyName": "小型号",
                "propertyNameId": 1102,
                "propertyValues": [
                    {
                        "isBasic": 0,
                        "isSelected": 1,
                        "order": 327,
                        "propertyValueId": 11452,
                        "propertyValueName": "A2275"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 319,
                        "propertyValueId": 5129,
                        "propertyValueName": "其他型号"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 325,
                        "propertyValueId": 11447,
                        "propertyValueName": "A2298"
                    },
                    {
                        "isBasic": 0,
                        "isSelected": 0,
                        "order": 326,
                        "propertyValueId": 11448,
                        "propertyValueName": "A2296"
                    }
                ]
            }
        ],
        "suggestRecyclePrice": 2187,
        "viceTitle": "大陆国行 | 红色 | A2275"
    },
    "resultMessage": ""
}

"""