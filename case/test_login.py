import unittest
import json
from ddt import ddt, data

from Mexcommon.RequestHttp import Request
from Mexcommon.WriteLogger import Log
from Mexcommon.login import login
from Mexcommon.RedConfig import red_
from Mexcommon.ptah_object import OsPath


@ddt
class Login(unittest.TestCase):
    # 请求的参数List
    AddressBook = [
        {"title": "存储注册时的设备信息(注册成功后调首页登录)saveDeviceInfo",
         "method": "post",
         "url": "/hc/app/userInfo/saveDeviceInfo",
         "body": {"adbEnabled": 0,
                  "androidId": "b109171b35c94873",
                  "availableStorage": " 37.3796GB",
                  "battery": "81",
                  "codeName": "REL",
                  "cpu": "arm64-v8a",
                  "cpuInfo": " ",
                  "cpuSpeed": "1989000KHz",
                  "currentWifi": "\"HAI-IT-5G\"",
                  "detailAddress": "",
                  "deviceLanguage": "zh",
                  "deviceMac": "D0:D2:C4:2F:54:3D",
                  "deviceModel": "OPPO#CPH1825",
                  "deviceSerial": "PR7TQS9SPZY5IN5T",
                  "deviceSoftwareVersion": "11",
                  "deviceVersionType": "user",
                  "displayMetrics": "1080,2196",
                  "fingerPrint": "OPPO/CPH1825/CPH1825:8.1.0/O11019/1539160089:user/release-keys",
                  "gaid": "null",
                  "hardware": "mt6771",
                  "imei": "354310678254322",
                  "imsi": "452050408783768",
                  "inDoor": -1,
                  "lag": "",
                  "lng": "",
                  "locationAddress": "",
                  "locationCity": "",
                  "mobileName": "OPPO F9 Pro",
                  "model": "OPPO#CPH1825",
                  "networkOperator": "",
                  "networkOperatorName": "",
                  "networkType": "wifi",
                  "operatorName": "中国移动,无服务",
                  "os": "8.1.0",
                  "phoneAvailableRam": " 3.4562GB",
                  "phoneCardNum": "",
                  "phoneOs": "Android",
                  "phoneTotalRam": "MemTotal:        5850108 kB",
                  "phonecardCount": 2,
                  "product": "CPH1825",
                  "radioVersion": "M_V3_P10,M_V3_P10",
                  "resolutionHeight": "2196",
                  "resolutionWidth": "1080",
                  "rooted": 0,
                  "routerMac": "f4:a4:d6:56:f9:94",
                  "runtimeAvailableMemory": " 0.3583GB",
                  "runtimeMaxMemory": " 0.3750GB",
                  "simState": 1,
                  "simulator": 0,
                  "timeZone": "GMT+08:00",
                  "totalStorage": " 50.1089GB",
                  "turnOnTime": "2022-10-18 09:33:08",
                  "uuid": "ba8a3ffc973faaea0009ef8aaf2f55fe4b271152a89d93aa36616ae1dbcf4ae0",
                  "uuidOriginal": "[-70, -118, 63, -4, -105, 63, -86, -22, 0, 9, -17, -118, -81, 47, 85, -2, 75, 39, "
                                  "17, 82, -88, -99, -109, -86, 54, 97, 106, -31, -37, -49, 74, -32]"}},
        {
            "title": "上传通讯录:AddressBook",
            "method": "post",
            "url": "/hc/app/userInfo/saveAddressBook",
            "body": [{
                "contactName": "Licenciado",
                "contactPhone": "+52 449 480 7440",
                "contactRelation": "",
                "lastTime": 1661998796390
            }, {
                "contactName": "1422firstcash",
                "contactPhone": "+52 449 482 0252",
                "contactRelation": "",
                "lastTime": 1661998844242
            }, {
                "contactName": "Vicente Ortiz",
                "contactPhone": "+52 449 496 9413",
                "contactRelation": "",
                "lastTime": 1661998880584
            }, {
                "contactName": "Orestamo",
                "contactPhone": "+52 449 507 7179",
                "contactRelation": "",
                "lastTime": 1661999049347
            }, {
                "contactName": "Aquella",
                "contactPhone": "+52 449 512 8518",
                "contactRelation": "",
                "lastTime": 1661999077020
            }, {
                "contactName": "Cash",
                "contactPhone": "+52 449 514 7208",
                "contactRelation": "",
                "lastTime": 1661999122287
            }]
        },
        {"title": "查询最大可借天数：queryAvailableProduct",
         "method": "post",
         "url": "/hc/app/loan/queryAvailableProduct",
         "body": {
             "dayRate": "0.77",
             "expectedInstallment": "0",
             "isNew": "1",
             "merchantNo": "01",
             "orgNo": "MEX",
             "prductPayAmountMax": "1300",
             "prductPayAmountMin": "300",
             "productAmount": "0",
             "productFastPayTime": "50",
             "productIntroduce": "testhhh",
             "productLoanTerm": "1",
             "productName": "Préstamos seguros",
             "productNo": "",
             "productPictureUrl": "/upload/image/20220803/2022080301312987180381.png",
             "productTerm": "0",
             "showPeriod": "0",
             "userExpectedAmount": "0",
             "userExpectedTerm": "0"}
         },
        {
            "title": "提交借款申请：submitOneProduct",
            "method": "post",
            "url": "/hc/app/market/submitOneProduct",
            "body": {
                "appList": [{
                    "appName": "MoonVay",
                    "appVersion": "1.0.5",
                    "firstInstallTime": "2022-05-16 10:00:43",
                    "lastUpdateTime": "2022-05-16 10:00:43",
                    "packageName": "app.moon.vay"
                }, {
                    "appName": "VayHome",
                    "appVersion": "2.2.8",
                    "firstInstallTime": "2022-08-01 11:19:09",
                    "lastUpdateTime": "2022-08-01 11:19:09",
                    "packageName": "com.hc.market"
                }, {
                    "appName": "Cola Credit",
                    "appVersion": "1.0.3",
                    "firstInstallTime": "2022-06-15 09:54:28",
                    "lastUpdateTime": "2022-06-15 09:54:28",
                    "packageName": "com.vicola.credit"
                }, {
                    "appName": "Loan Quick",
                    "appVersion": "1.0.9",
                    "firstInstallTime": "2022-09-28 16:15:57",
                    "lastUpdateTime": "2022-09-28 16:15:57",
                    "packageName": "com.loan.quick"
                }, {
                    "appName": "蓝灯",
                    "appVersion": "6.8.10 (20210920.160125)",
                    "firstInstallTime": "2022-02-10 16:25:10",
                    "lastUpdateTime": "2022-02-10 16:25:10",
                    "packageName": "org.getlantern.lantern"
                }, {
                    "appName": "搜狗输入法",
                    "appVersion": "11.3",
                    "firstInstallTime": "2022-05-10 17:06:04",
                    "lastUpdateTime": "2022-05-10 17:06:04",
                    "packageName": "com.sohu.inputmethod.sogou"
                }, {
                    "appName": "Vietnamese Spam Filtering Engine",
                    "appVersion": "1.0.6",
                    "firstInstallTime": "2015-01-01 00:04:47",
                    "lastUpdateTime": "2015-01-01 00:04:47",
                    "packageName": "com.svmc.spamengine"
                }, {
                    "appName": "Sky Pesa",
                    "appVersion": "1.0.7",
                    "firstInstallTime": "2022-06-24 11:50:38",
                    "lastUpdateTime": "2022-06-24 11:50:38",
                    "packageName": "sky.pesa"
                }, {
                    "appName": "GoldFish88",
                    "appVersion": "2.1.1",
                    "firstInstallTime": "2022-02-10 16:15:41",
                    "lastUpdateTime": "2022-02-10 16:15:41",
                    "packageName": "com.goldfish88.club"
                }, {
                    "appName": "Cash Star",
                    "appVersion": "1.0",
                    "firstInstallTime": "2022-09-22 12:18:00",
                    "lastUpdateTime": "2022-09-22 12:18:00",
                    "packageName": "com.ph.cashstar"
                }, {
                    "appName": "mex_af_test",
                    "appVersion": "1.0.8",
                    "firstInstallTime": "2022-10-08 12:12:29",
                    "lastUpdateTime": "2022-10-08 12:12:29",
                    "packageName": "mex.af.test"
                }, {
                    "appName": "Vay Dễ",
                    "appVersion": "2.0.3",
                    "firstInstallTime": "2022-01-17 12:18:37",
                    "lastUpdateTime": "2022-01-17 12:18:37",
                    "packageName": "com.vn.easycash"
                }, {
                    "appName": "com.samsung.updatecarriermatch",
                    "appVersion": "1.0.5",
                    "firstInstallTime": "2015-01-01 00:04:37",
                    "lastUpdateTime": "2015-01-01 00:04:37",
                    "packageName": "com.samsung.updatecarriermatch"
                }, {
                    "appName": "贴吧极速版",
                    "appVersion": "9.1.0.0",
                    "firstInstallTime": "2022-07-22 16:45:32",
                    "lastUpdateTime": "2022-07-22 16:45:32",
                    "packageName": "com.baidu.tieba_mini"
                }, {
                    "appName": "Vysor",
                    "appVersion": "4.1.58",
                    "firstInstallTime": "2022-04-28 16:20:45",
                    "lastUpdateTime": "2022-04-28 16:20:45",
                    "packageName": "com.koushikdutta.vysor"
                }, {
                    "appName": "V-Credit",
                    "appVersion": "1.0.3",
                    "firstInstallTime": "2022-02-10 18:13:38",
                    "lastUpdateTime": "2022-02-10 18:13:38",
                    "packageName": "com.vi.vcredit"
                }, {
                    "appName": "Tiki",
                    "appVersion": "4.91.2",
                    "firstInstallTime": "2022-02-10 16:17:02",
                    "lastUpdateTime": "2022-02-10 16:17:02",
                    "packageName": "vn.tiki.app.tikiandroid"
                }, {
                    "appName": "生活钱包",
                    "appVersion": "1.0.3",
                    "firstInstallTime": "2022-09-26 11:10:09",
                    "lastUpdateTime": "2022-09-26 11:10:09",
                    "packageName": "com.life.wallet"
                }, {
                    "appName": "VnExpress",
                    "appVersion": "9.0.0",
                    "firstInstallTime": "2022-02-10 15:57:05",
                    "lastUpdateTime": "2022-02-10 16:18:34",
                    "packageName": "fr.playsoft.vnexpress"
                }, {
                    "appName": "Handy Cash",
                    "appVersion": "1.0.0",
                    "firstInstallTime": "2022-02-17 17:09:38",
                    "lastUpdateTime": "2022-02-18 09:38:56",
                    "packageName": "handy.cash.ph"
                }, {
                    "appName": "MoMo",
                    "appVersion": "3.1.4",
                    "firstInstallTime": "2022-01-28 14:11:58",
                    "lastUpdateTime": "2022-01-28 14:11:58",
                    "packageName": "com.mservice.momotransfer"
                }, {
                    "appName": "PandaVPN",
                    "appVersion": "6.4.0",
                    "firstInstallTime": "2022-09-06 09:39:00",
                    "lastUpdateTime": "2022-09-06 09:39:00",
                    "packageName": "com.pandavpn.androidproxy"
                }, {
                    "appName": "Care Finance",
                    "appVersion": "1.1",
                    "firstInstallTime": "2022-08-03 14:45:12",
                    "lastUpdateTime": "2022-08-03 14:45:12",
                    "packageName": "care.finance"
                }, {
                    "appName": "Foxpay",
                    "appVersion": "2.4.9",
                    "firstInstallTime": "2022-02-10 16:15:19",
                    "lastUpdateTime": "2022-02-10 16:15:19",
                    "packageName": "com.ftel.foxpay"
                }, {
                    "appName": "Hinance",
                    "appVersion": "1.0.8",
                    "firstInstallTime": "2022-10-08 18:28:09",
                    "lastUpdateTime": "2022-10-08 18:28:09",
                    "packageName": "com.mx.hinance"
                }, {
                    "appName": "ZaloPay",
                    "appVersion": "7.2.0",
                    "firstInstallTime": "2022-02-10 16:16:38",
                    "lastUpdateTime": "2022-02-10 16:16:38",
                    "packageName": "vn.com.vng.zalopay"
                }, {
                    "appName": "Báo Mới",
                    "appVersion": "22.01",
                    "firstInstallTime": "2022-02-10 16:17:58",
                    "lastUpdateTime": "2022-02-10 16:17:58",
                    "packageName": "com.epi"
                }, {
                    "appName": "GoldHouse",
                    "appVersion": "1.0",
                    "firstInstallTime": "2022-08-17 18:31:18",
                    "lastUpdateTime": "2022-08-17 18:31:18",
                    "packageName": "com.hc.gh"
                }, {
                    "appName": "Cây phát tài",
                    "appVersion": "1.5.8",
                    "firstInstallTime": "2022-07-25 10:56:16",
                    "lastUpdateTime": "2022-07-25 10:56:16",
                    "packageName": "com.hc.mt"
                }, {
                    "appName": "Sendo",
                    "appVersion": "4.0.44",
                    "firstInstallTime": "2022-02-10 16:16:10",
                    "lastUpdateTime": "2022-02-10 16:16:10",
                    "packageName": "com.sendo"
                }, {
                    "appName": "Support",
                    "appVersion": "2.5.1",
                    "firstInstallTime": "2022-09-21 19:06:13",
                    "lastUpdateTime": "2022-09-21 19:06:13",
                    "packageName": "support.ph.com"
                }, {
                    "appName": "Ví liên kết",
                    "appVersion": "1.0.6",
                    "firstInstallTime": "2022-06-27 17:15:49",
                    "lastUpdateTime": "2022-06-27 17:15:49",
                    "packageName": "com.vietnam.wallet"
                }, {
                    "appName": "Shopee",
                    "appVersion": "2.82.33",
                    "firstInstallTime": "2022-02-10 16:17:39",
                    "lastUpdateTime": "2022-02-10 16:17:39",
                    "packageName": "com.shopee.vn"
                }, {
                    "appName": "Smart Tutor",
                    "appVersion": "1.5 (build 212)",
                    "firstInstallTime": "2015-01-01 00:04:45",
                    "lastUpdateTime": "2015-01-01 00:04:45",
                    "packageName": "com.rsupport.rs.activity.rsupport.aas2"
                }, {
                    "appName": "Galaxy Gift",
                    "appVersion": "3.1",
                    "firstInstallTime": "2015-01-01 00:04:50",
                    "lastUpdateTime": "2015-01-01 00:04:50",
                    "packageName": "com.samsungvietnam.quatanggalaxy"
                }, {
                    "appName": "Hiland Credit",
                    "appVersion": "1.5.8",
                    "firstInstallTime": "2022-08-31 17:35:38",
                    "lastUpdateTime": "2022-08-31 17:35:38",
                    "packageName": "com.hc.credit"
                }, {
                    "appName": "OpenPurse",
                    "appVersion": "1.0.0",
                    "firstInstallTime": "2022-09-30 10:28:17",
                    "lastUpdateTime": "2022-09-30 10:28:17",
                    "packageName": "com.mexico.loan.open.purse"
                }, {
                    "appName": "Dodo Cash",
                    "appVersion": "1.0.0",
                    "firstInstallTime": "2022-07-19 19:02:00",
                    "lastUpdateTime": "2022-07-19 19:02:00",
                    "packageName": "com.dodocash.android"
                }],
                "applyLoanAmount": "750.00",
                "attach": [{
                    "attachName": "/upload/image/20221008",
                    "channel": "app",
                    "md5": "EEE599F98D70FFBC13723AE745195E39",
                    "newName": "2022100821304451988042.jpeg",
                    "newPathName": "/upload/image/20221008/2022100821304451988042.jpeg",
                    "originalAttachName": "/upload/image/20221008",
                    "originalName": "1665282642516677.jpeg",
                    "path": "/upload/image/20221008",
                    "purpose": "sfzzm",
                    "size": 6773,
                    "uploadType": "image"
                }, {
                    "attachName": "/upload/image/20221008",
                    "channel": "app",
                    "md5": "5A06625DB80E94064A554A4E66C7EA30",
                    "newName": "2022100821305252024434.jpeg",
                    "newPathName": "/upload/image/20221008/2022100821305252024434.jpeg",
                    "originalAttachName": "/upload/image/20221008",
                    "originalName": "166528265116280.jpeg",
                    "path": "/upload/image/20221008",
                    "purpose": "sfzfm",
                    "size": 6769,
                    "uploadType": "image"
                }, {
                    "attachName": "/upload/image/20221008",
                    "channel": "app",
                    "md5": "D0F4E50BB34810F395B2B8CA1DCC67D0",
                    "newName": "2022100821333752185605.jpeg",
                    "newPathName": "/upload/image/20221008/2022100821333752185605.jpeg",
                    "originalAttachName": "/upload/image/20221008",
                    "originalName": "166528281559549.jpeg",
                    "path": "/upload/image/20221008",
                    "purpose": "scsfz",
                    "size": 6840,
                    "uploadType": "image"
                }],
                "bank": {
                    "idCard": "G21508648658548558"
                },
                "base": {
                    "birthday": "1993-01-01",
                    "childNum": "1",
                    "education": "2",
                    "email": "hvhhvhh@163.com",
                    "familyName": "fade",
                    "givenName": "fave",
                    "idCardNum": "G21508648658548558",
                    "instancyContacts": [{
                        "contactName": "13wei(*´I`*)",
                        "contactPhone": "+529212975512",
                        "contactRelation": "0",
                        "lastTime": 0
                    }, {
                        "contactName": "13wei02(／_＼)大怨种",
                        "contactPhone": "525524064428",
                        "contactRelation": "2",
                        "lastTime": 0
                    }],
                    "maritalStatus": "1",
                    "middleName": "here",
                    "placeAddress": "hcbh",
                    "placeCity": "001011",
                    "placeProvince": "001",
                    "placeTime": "",
                    "postalCode": "",
                    "rfc": "",
                    "sex": "1",
                    "sysPlaceAddress": "",
                    "uname": "",
                    "whatsApp": "2158635665"
                },
                "configPayout": "true",
                "customerSource": "com.mx.hinance",
                "firstExpectAmount": "750.00",
                "firstExpectDay": "10",
                "livenessId": "",
                "merchantNo": "01",
                "orgNo": "MEX",
                "payoutPaymentConfig": {
                    "bankConfig": {
                        "accountType": {
                            "label": "银行",
                            "value": "0"
                        },
                        "bankCard": "1258638668658668",
                        "bankType": {
                            "label": "BANCOMEXT",
                            "value": "37006"
                        },
                        "name": "fade fave here"
                    },
                    "paymentChildKey": {
                        "label": "Bank",
                        "value": "bank"
                    },
                    "paymentTypeKey": {
                        "label": "Bank transfer",
                        "value": "bank"
                    }
                },
                "productNo": "MEX_01_1_20220927173142",
                "promotionChannels": "googlePlay",
                "sign": {
                    "adbEnabled": 1,
                    "androidId": "4535c1db08e9d00f",
                    "availableStorage": " 16.0592GB",
                    "battery": "48",
                    "codeName": "REL",
                    "cpu": "armeabi-v7a",
                    "cpuInfo": "",
                    "cpuSpeed": "1586000KHz",
                    "currentWifi": "\"HCLOUD-Risk\"",
                    "detailAddress": "",
                    "deviceLanguage": "zh",
                    "deviceMac": "BC:76:5E:8A:0F:91",
                    "deviceModel": "samsung#SM-G610F",
                    "deviceSerial": "3300fbcb8a7783cb",
                    "deviceSoftwareVersion": "01",
                    "deviceVersionType": "user",
                    "displayMetrics": "1080,1920",
                    "fingerPrint": "samsung/on7xeltedd/on7xelte:8.1.0/M1AJQ/G610FDXS1CTE1:user/release-keys",
                    "gaid": "null",
                    "hardware": "samsungexynos7870",
                    "imei": "353415087834233",
                    "imsi": "",
                    "inDoor": -1,
                    "lag": "",
                    "lng": "",
                    "locationAddress": "",
                    "locationCity": "",
                    "mobileName": "Galaxy J7 Prime",
                    "model": "samsung#SM-G610F",
                    "networkOperator": "46000",
                    "networkOperatorName": "",
                    "networkType": "wifi",
                    "operatorName": "",
                    "os": "8.1.0",
                    "phoneAvailableRam": " 0.9205GB",
                    "phoneCardNum": "",
                    "phoneOs": "Android",
                    "phoneTotalRam": "MemTotal:        2882568 kB",
                    "phonecardCount": 0,
                    "product": "on7xeltedd",
                    "radioVersion": "G610FDDS1CTE2",
                    "resolutionHeight": "1920",
                    "resolutionWidth": "1080",
                    "rooted": 0,
                    "routerMac": "3c:cd:5d:11:42:30",
                    "runtimeAvailableMemory": " 0.1720GB",
                    "runtimeMaxMemory": " 0.1875GB",
                    "simState": 0,
                    "simulator": 1,
                    "timeZone": "GMT+08:00",
                    "totalStorage": " 25.3557GB",
                    "turnOnTime": "2022-09-28 10:10:51",
                    "uuid": "53454350484f4e455f3030303030303030303030303030303030313632313535",
                    "uuidOriginal": "[83, 69, 67, 80, 72, 79, 78, 69, 95, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, "
                                    "48, 48, 48, 48, 48, 48, 49, 54, 50, 49, 53, 53] "
                },
                "work": {
                    "income": "4",
                    "payDay": "10",
                    "post": "0",
                    "salaryType": "3",
                    "secondPayDay": "",
                    "sourceIncome": "0",
                    "tel": "",
                    "workTime": "1"
                }
            }}

    ]

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化一次 注册登录，写个新的token进配置文件
        login().login()

        cls.header = {
            'app-name': 'Hinance',
            'app-version': '1.0.7',
            'channel': 'googlePlay',
            'commercialId': '1',
            'lang': 'zh',
            'organizationId': 'DCMEX',
            'token': red_(OsPath.Basfig_path).red_get('token', 'token_'),
            'Content-Type': 'application/json'
        }

    def setUp(self) -> None:
        Log().debug('================================开始================================')

    @data(*AddressBook)
    def test_UploadingAddressBook(self, Book):
        try:
            resp = Request(Book['method'], url_=Book['url'],
                           body_=json.dumps(Book['body']),
                           headers_=self.header,
                           cookies=None).get_json()
            if resp['code'] == 0 and resp['msg'] == '成功':
                Log().debug('\n当前请求接口是: {0},\n请求参数: {1},\n请求结果{2}'.format(Book['title'], Book['body'], resp))
            else:
                Log().debug('当前接口：{0},响应结果{1},错误id：{2}'.format(Book['title'], resp['msg'], resp['traceId']))
                Log().info('当前接口：{0},响应结果{1},错误id：{2}'.format(Book['title'], resp['msg'], resp['traceId']))
                Log().error('\n当前请求接口是: {0},\n请求参数: {1},\n请求结果{2}'.format(Book['title'], Book['body'], resp))

            # 接口断言
            self.assertEqual('成功', resp['msg'])

        except Exception as e:
            Log().error("当前请求的错误: {}".format(e))
            raise e

    def test_submitOneProduct(self):
        pass

    def tearDown(self) -> None:
        Log().debug('================================结束================================\n')


if __name__ == '__main__':
    unittest.main()
