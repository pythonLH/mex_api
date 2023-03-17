import json
from apiMethod.common.request_ import Request
from apiMethod.common.config_ import red_
from apiMethod.common.logger_ import Log
from apiMethod.ospath.ConfigurePaths import Basfig_path
from apiMethod.login_ import login


class Test_applyOrder:

    def setup_class(self):
        # 前置方法中，调用注册登录接口，祈祷(菩萨保佑)生成最新的token
        login().login()

    def teardown_class(self):
        pass

    headers = {'app-name': 'Hinance',
               'app-version': '1.0.7',
               'channel': 'googlePlay',
               'commercialId': '01',
               'lang': 'zh',
               'organizationId': 'DCMEX',
               'token': red_(Basfig_path).red_get('token', 'token_'),
               'Content-Type': 'application/json'}

    def test_saveDeviceInfo(self):
        url = r"/hc/app/userInfo/saveDeviceInfo"
        payload = json.dumps({
            "adbEnabled": 0,
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
            "uuidOriginal": "[-70, -118, 63, -4, -105, 63, -86, -22, 0, 9, -17, -118, -81, 47, 85, -2, 75, 39, 17, "
                            "82, -88, -99, -109, -86, 54, 97, 106, -31, -37, -49, 74, -32] "
        })
        try:
            response = Request('post', url_=url, body_=payload, headers_=self.headers, cookies=None).get_json()
        except Exception as e:
            Log().error("请求接口报错：{0}".format(e))
            raise e
        assert 0 == response["code"]
        assert "成功" == response["msg"]
        assert True is response["success"]

    def test_queryAvailableProduct(self):
        url = r"/hc/app/loan/queryAvailableProduct"
        payload = json.dumps({
            "dayRate": "0.77",
            "expectedInstallment": 0,
            "isNew": "1",
            "merchantNo": "01",
            "orgNo": "MEX",
            "prductPayAmountMax": 1300,
            "prductPayAmountMin": 300,
            "productAmount": 0,
            "productFastPayTime": "50",
            "productIntroduce": "testhhh",
            "productLoanTerm": "1",
            "productName": "Préstamos seguros",
            "productNo": "",
            "productPictureUrl": "/upload/image/20220803/2022080301312987180381.png",
            "productTerm": 0,
            "showPeriod": 0,
            "userExpectedAmount": 0,
            "userExpectedTerm": 0
        })
        try:
            response = Request('post', url_=url, body_=payload, headers_=self.headers, cookies=None).get_json()
        except Exception as e:
            Log().error("请求接口报错：{0}".format(e))
            raise e
        assert 0 == response["code"]
        assert "成功" == response["msg"]
        assert True is response["success"]

    def test_saveAddressBook(self):

        url = r"/hc/app/userInfo/saveAddressBook"

        payload = json.dumps([
            {
                "contactName": "Aquella",
                "contactPhone": "+524495128518",
                "contactRelation": "",
                "lastTime": "1661999077020"
            },
            {
                "contactName": "Cash",
                "contactPhone": "+524495147208",
                "contactRelation": "",
                "lastTime": "1661999122287"
            }
        ])
        try:
            response = Request('post', url_=url, body_=payload, headers_=self.headers, cookies=None).get_json()
        except Exception as e:
            Log().error("请求接口报错：{0}".format(e))
            raise e

        assert 0 == response["code"]
        assert "成功" == response["msg"]
        assert True is response["success"]

    def test_submitOneProduct(self):
        url = r"/hc/app/market/submitOneProduct"
        payload = json.dumps({
            "appList": [
                {
                    "appName": "亚马逊购物",
                    "appVersion": "18.19.0.100",
                    "firstInstallTime": "2020-11-20 19:18:44",
                    "lastUpdateTime": "2020-11-20 19:18:44",
                    "packageName": "com.amazon.mShop.android.shopping"
                },
                {
                    "appName": "Dust Settle",
                    "appVersion": "2.14",
                    "firstInstallTime": "2020-11-20 19:19:05",
                    "lastUpdateTime": "2022-09-10 13:47:16",
                    "packageName": "com.logame.eliminateintruder3d"
                },
                {
                    "appName": "VayHome",
                    "appVersion": "2.3.4",
                    "firstInstallTime": "2022-08-11 16:50:57",
                    "lastUpdateTime": "2022-08-11 16:50:57",
                    "packageName": "com.hc.market"
                },
                {
                    "appName": "Crazy Juicer",
                    "appVersion": "1.4.7",
                    "firstInstallTime": "2020-11-20 19:19:02",
                    "lastUpdateTime": "2022-08-15 21:14:09",
                    "packageName": "com.crazy.juicer.xm"
                },
                {
                    "appName": "Cola Credit",
                    "appVersion": "1.0.0",
                    "firstInstallTime": "2022-04-13 14:49:42",
                    "lastUpdateTime": "2022-04-13 14:49:42",
                    "packageName": "com.vicola.credit"
                },
                {
                    "appName": "小米文档查看器（WPS定制）",
                    "appVersion": "2.5.3",
                    "firstInstallTime": "2020-09-22 01:19:46",
                    "lastUpdateTime": "2020-09-22 01:19:46",
                    "packageName": "cn.wps.xiaomi.abroad.lite"
                },
                {
                    "appName": "VK",
                    "appVersion": "7.19",
                    "firstInstallTime": "2022-08-12 10:36:57",
                    "lastUpdateTime": "2022-08-12 10:36:57",
                    "packageName": "com.vkontakte.android"
                },
                {
                    "appName": "Block Puzzle Guardian",
                    "appVersion": "2.1.47",
                    "firstInstallTime": "2020-11-20 19:18:55",
                    "lastUpdateTime": "2022-08-15 21:13:19",
                    "packageName": "com.block.puzzle.game.hippo.mi"
                },
                {
                    "appName": "F@st Mobile",
                    "appVersion": "1.3.0.2",
                    "firstInstallTime": "2020-12-24 17:33:09",
                    "lastUpdateTime": "2022-08-18 19:30:38",
                    "packageName": "com.fastacash.tcb"
                },
                {
                    "appName": "Zalo",
                    "appVersion": "22.04.01",
                    "firstInstallTime": "2022-05-10 19:56:06",
                    "lastUpdateTime": "2022-05-10 19:56:06",
                    "packageName": "com.zing.zalo"
                },
                {
                    "appName": "蓝灯",
                    "appVersion": "6.8.10 (20210920.160125)",
                    "firstInstallTime": "2022-03-11 14:37:06",
                    "lastUpdateTime": "2022-03-11 14:37:06",
                    "packageName": "org.getlantern.lantern"
                },
                {
                    "appName": "Google 播客",
                    "appVersion": "1.0.0.266384425",
                    "firstInstallTime": "2020-11-20 19:19:49",
                    "lastUpdateTime": "2020-11-20 19:19:49",
                    "packageName": "com.google.android.apps.podcasts"
                },
                {
                    "appName": "CameraX Basic",
                    "appVersion": "1.0.0",
                    "firstInstallTime": "2022-05-13 18:06:37",
                    "lastUpdateTime": "2022-05-13 18:06:37",
                    "packageName": "com.android.example.cameraxbasic"
                },
                {
                    "appName": "BooCash",
                    "appVersion": "1.0.0",
                    "firstInstallTime": "2022-05-13 11:12:12",
                    "lastUpdateTime": "2022-05-13 11:12:12",
                    "packageName": "com.boo.cash"
                },
                {
                    "appName": "Vay Dễ",
                    "appVersion": "2.0.3",
                    "firstInstallTime": "2022-03-28 11:07:01",
                    "lastUpdateTime": "2022-03-28 11:07:01",
                    "packageName": "com.vn.easycash"
                },
                {
                    "appName": "TCB OTP",
                    "appVersion": "1.2.3",
                    "firstInstallTime": "2020-12-24 17:54:01",
                    "lastUpdateTime": "2022-05-23 11:22:50",
                    "packageName": "com.techcombank.stk.corp"
                },
                {
                    "appName": "Max Loan",
                    "appVersion": "1.2",
                    "firstInstallTime": "2021-12-29 18:05:28",
                    "lastUpdateTime": "2022-01-05 18:26:46",
                    "packageName": "com.ph.maxloan"
                },
                {
                    "appName": "贴吧极速版",
                    "appVersion": "9.1.0.0",
                    "firstInstallTime": "2022-08-12 10:31:30",
                    "lastUpdateTime": "2022-08-12 10:31:30",
                    "packageName": "com.baidu.tieba_mini"
                },
                {
                    "appName": "Fat Cash",
                    "appVersion": "1.6",
                    "firstInstallTime": "2021-11-16 14:13:26",
                    "lastUpdateTime": "2021-11-16 14:13:26",
                    "packageName": "com.vi.clouds.fatcash"
                },
                {
                    "appName": "Duo",
                    "appVersion": "68.0.284888502.DR68_RC09",
                    "firstInstallTime": "2020-11-20 19:19:26",
                    "lastUpdateTime": "2020-11-20 19:19:26",
                    "packageName": "com.google.android.apps.tachyon"
                },
                {
                    "appName": "Vysor",
                    "appVersion": "4.2.2",
                    "firstInstallTime": "2022-07-14 14:42:21",
                    "lastUpdateTime": "2022-07-14 14:42:21",
                    "packageName": "com.koushikdutta.vysor"
                },
                {
                    "appName": "锁屏画报",
                    "appVersion": "V7-G-220809",
                    "firstInstallTime": "2020-09-22 01:19:46",
                    "lastUpdateTime": "2022-08-17 05:01:01",
                    "packageName": "com.miui.android.fashiongallery"
                },
                {
                    "appName": "FbPushDemo",
                    "appVersion": "1.0",
                    "firstInstallTime": "2022-07-20 16:01:29",
                    "lastUpdateTime": "2022-08-18 10:17:56",
                    "packageName": "com.hc.fbpushdemo"
                },
                {
                    "appName": "TIM",
                    "appVersion": "3.4.4",
                    "firstInstallTime": "2022-03-18 14:38:00",
                    "lastUpdateTime": "2022-03-18 14:38:00",
                    "packageName": "com.tencent.tim"
                },
                {
                    "appName": "Lazada",
                    "appVersion": "6.43.0",
                    "firstInstallTime": "2020-11-20 19:17:59",
                    "lastUpdateTime": "2020-11-20 19:17:59",
                    "packageName": "com.lazada.android"
                },
                {
                    "appName": "生活钱包",
                    "appVersion": "1.0.3",
                    "firstInstallTime": "2022-09-19 16:18:28",
                    "lastUpdateTime": "2022-09-19 16:18:28",
                    "packageName": "com.life.wallet"
                },
                {
                    "appName": "云端硬盘",
                    "appVersion": "2.19.472.05.34",
                    "firstInstallTime": "2020-11-20 19:19:20",
                    "lastUpdateTime": "2020-11-20 19:19:20",
                    "packageName": "com.google.android.apps.docs"
                },
                {
                    "appName": "蚂蚁盒子",
                    "appVersion": "1.1.0",
                    "firstInstallTime": "2022-07-12 16:43:14",
                    "lastUpdateTime": "2022-07-12 16:43:14",
                    "packageName": "com.vn.antbox"
                },
                {
                    "appName": "芒果游戏翻译",
                    "appVersion": "2.4.6",
                    "firstInstallTime": "2022-04-13 15:46:24",
                    "lastUpdateTime": "2022-04-13 15:46:24",
                    "packageName": "com.mg.yurao"
                },
                {
                    "appName": "Mobile Device Information Provider",
                    "appVersion": "1.0.200119.0_112210",
                    "firstInstallTime": "2020-11-20 19:18:27",
                    "lastUpdateTime": "2020-11-20 19:18:27",
                    "packageName": "com.amazon.appmanager"
                },
                {
                    "appName": "TikTok",
                    "appVersion": "25.9.4",
                    "firstInstallTime": "2022-05-23 12:08:51",
                    "lastUpdateTime": "2022-09-07 15:08:25",
                    "packageName": "com.ss.android.ugc.trill"
                },
                {
                    "appName": "MyLoan",
                    "appVersion": "1.1",
                    "firstInstallTime": "2021-11-16 14:10:56",
                    "lastUpdateTime": "2021-11-16 14:10:56",
                    "packageName": "com.ph.loan.myloan"
                },
                {
                    "appName": "Google Play 电影",
                    "appVersion": "4.17.34",
                    "firstInstallTime": "2020-11-20 19:19:50",
                    "lastUpdateTime": "2020-11-20 19:19:50",
                    "packageName": "com.google.android.videos"
                },
                {
                    "appName": "Mi Community",
                    "appVersion": "4.5.2",
                    "firstInstallTime": "2020-11-20 19:19:35",
                    "lastUpdateTime": "2020-11-20 19:19:35",
                    "packageName": "com.mi.global.bbs"
                },
                {
                    "appName": "Netflix",
                    "appVersion": "8.39.0 build 9 50265",
                    "firstInstallTime": "2020-11-20 19:18:16",
                    "lastUpdateTime": "2022-09-07 15:09:53",
                    "packageName": "com.netflix.mediaclient"
                },
                {
                    "appName": "PandaVPN",
                    "appVersion": "6.2.0",
                    "firstInstallTime": "2022-03-11 14:33:04",
                    "lastUpdateTime": "2022-06-29 16:34:10",
                    "packageName": "com.pandavpn.androidproxy"
                },
                {
                    "appName": "方块对对碰",
                    "appVersion": "1.9.4",
                    "firstInstallTime": "2020-11-20 19:19:10",
                    "lastUpdateTime": "2022-08-18 13:12:19",
                    "packageName": "com.mintgames.triplecrush.tile.fun"
                },
                {
                    "appName": "Facebook",
                    "appVersion": "stub (55.1.0)",
                    "firstInstallTime": "2020-11-20 19:18:42",
                    "lastUpdateTime": "2020-11-20 19:18:42",
                    "packageName": "com.facebook.katana"
                },
                {
                    "appName": "Hinance",
                    "appVersion": "1.0.7",
                    "firstInstallTime": "2022-09-20 10:44:41",
                    "lastUpdateTime": "2022-09-20 10:44:41",
                    "packageName": "com.mx.hinance"
                },
                {
                    "appName": "MIYA",
                    "appVersion": "4.0.1",
                    "firstInstallTime": "2022-04-28 15:18:55",
                    "lastUpdateTime": "2022-04-28 15:18:55",
                    "packageName": "com.airlive.miya"
                },
                {
                    "appName": "Cây phát tài",
                    "appVersion": "1.5.9",
                    "firstInstallTime": "2022-08-18 18:28:36",
                    "lastUpdateTime": "2022-08-18 18:28:36",
                    "packageName": "com.hc.mt"
                },
                {
                    "appName": "CameraX Basic",
                    "appVersion": "1.0.1",
                    "firstInstallTime": "2022-05-13 15:40:03",
                    "lastUpdateTime": "2022-05-13 18:03:21",
                    "packageName": "com.hc.hicloudcamerasdk"
                },
                {
                    "appName": "领英",
                    "appVersion": "1.1.2",
                    "firstInstallTime": "2020-11-20 19:18:43",
                    "lastUpdateTime": "2020-11-20 19:18:43",
                    "packageName": "com.linkedin.android"
                },
                {
                    "appName": "越南",
                    "appVersion": "1.1.2",
                    "firstInstallTime": "2021-10-21 15:37:25",
                    "lastUpdateTime": "2021-10-21 15:37:25",
                    "packageName": "com.vi.mpt"
                },
                {
                    "appName": "Bubble Shooter And Friends",
                    "appVersion": "1.5.8",
                    "firstInstallTime": "2020-11-20 19:19:15",
                    "lastUpdateTime": "2022-09-10 06:47:10",
                    "packageName": "com.sukhavati.gotoplaying.bubble.BubbleShooter.mint"
                },
                {
                    "appName": "Booking.com缤客",
                    "appVersion": "21.4.100",
                    "firstInstallTime": "2020-11-20 19:18:17",
                    "lastUpdateTime": "2020-11-20 19:18:17",
                    "packageName": "com.booking"
                },
                {
                    "appName": "Mi Credit",
                    "appVersion": "1.1.0.779",
                    "firstInstallTime": "2020-09-22 01:19:46",
                    "lastUpdateTime": "2022-01-29 09:57:47",
                    "packageName": "com.micredit.in"
                },
                {
                    "appName": "mSign",
                    "appVersion": "21.1",
                    "firstInstallTime": "2020-12-23 18:50:51",
                    "lastUpdateTime": "2022-07-13 14:44:04",
                    "packageName": "vn.com.sacombank.msign"
                },
                {
                    "appName": "Trip.com",
                    "appVersion": "7.5.1",
                    "firstInstallTime": "2020-12-31 13:38:58",
                    "lastUpdateTime": "2020-12-31 13:38:58",
                    "packageName": "ctrip.english"
                },
                {
                    "appName": "YouTube Music",
                    "appVersion": "3.45.54",
                    "firstInstallTime": "2020-11-20 19:19:55",
                    "lastUpdateTime": "2020-11-20 19:19:55",
                    "packageName": "com.google.android.apps.youtube.music"
                },
                {
                    "appName": "AirDroid Cast",
                    "appVersion": "1.0.3.2",
                    "firstInstallTime": "2022-04-27 10:49:59",
                    "lastUpdateTime": "2022-04-27 10:49:59",
                    "packageName": "com.sand.aircast"
                },
                {
                    "appName": "Google 新闻",
                    "appVersion": "5.16.0.19092025",
                    "firstInstallTime": "2020-11-20 19:19:30",
                    "lastUpdateTime": "2020-11-20 19:19:30",
                    "packageName": "com.google.android.apps.magazines"
                },
                {
                    "appName": "MiDrive",
                    "appVersion": "0.0.1",
                    "firstInstallTime": "2020-09-22 01:19:46",
                    "lastUpdateTime": "2020-09-22 01:19:46",
                    "packageName": "com.miui.newmidrive"
                },
                {
                    "appName": "Hiland Credit",
                    "appVersion": "1.5.8",
                    "firstInstallTime": "2022-08-11 14:53:40",
                    "lastUpdateTime": "2022-09-20 03:19:24",
                    "packageName": "com.hc.credit"
                },
                {
                    "appName": "CameraXDemo",
                    "appVersion": "1.0",
                    "firstInstallTime": "2022-07-22 17:50:30",
                    "lastUpdateTime": "2022-07-22 17:50:30",
                    "packageName": "com.example.cameraxdemo"
                },
                {
                    "appName": "OpenPurse",
                    "appVersion": "1.0.0",
                    "firstInstallTime": "2022-09-09 21:28:24",
                    "lastUpdateTime": "2022-09-09 21:28:24",
                    "packageName": "com.mexico.loan.open.purse"
                },
                {
                    "appName": "WPS Office",
                    "appVersion": "12.3.1",
                    "firstInstallTime": "2020-11-20 19:18:28",
                    "lastUpdateTime": "2020-11-20 19:18:28",
                    "packageName": "cn.wps.moffice_eng"
                },
                {
                    "appName": "Lemon Peso",
                    "appVersion": "1.7.0",
                    "firstInstallTime": "2022-01-13 14:56:17",
                    "lastUpdateTime": "2022-01-13 15:02:09",
                    "packageName": "com.hc.ph.lemon"
                },
                {
                    "appName": "Dodo Cash",
                    "appVersion": "1.0.0",
                    "firstInstallTime": "2022-07-19 16:57:16",
                    "lastUpdateTime": "2022-07-19 16:57:16",
                    "packageName": "com.dodocash.android"
                }
            ],
            "applyLoanAmount": "1000.00",
            "attach": [
                {
                    "attachName": "/upload/file/20220920",
                    "channel": "app",
                    "md5": "0D600E05EC18531C8E67EE69480EDDCB",
                    "newName": "202209200141534441373.jpg",
                    "newPathName": "/upload/file/20220920/202209200141534441373.jpg",
                    "originalAttachName": "/upload/file/20220920",
                    "originalName": "2022-09-20-14-41-49-250.jpg",
                    "path": "/upload/file/20220920",
                    "purpose": "sfzzm",
                    "size": 523576,
                    "uploadType": "file"
                },
                {
                    "attachName": "/upload/file/20220920",
                    "channel": "app",
                    "md5": "A6ECB34FA5D80503CFA623DF8451106B",
                    "newName": "202209200142084557284.jpg",
                    "newPathName": "/upload/file/20220920/202209200142084557284.jpg",
                    "originalAttachName": "/upload/file/20220920",
                    "originalName": "2022-09-20-14-42-03-983.jpg",
                    "path": "/upload/file/20220920",
                    "purpose": "sfzfm",
                    "size": 499401,
                    "uploadType": "file"
                },
                {
                    "attachName": "/upload/file/20220920",
                    "channel": "app",
                    "md5": "9D1D7D5A9A9B950E1B1A07B95727892B",
                    "newName": "202209200143034656117.jpg",
                    "newPathName": "/upload/file/20220920/202209200143034656117.jpg",
                    "originalAttachName": "/upload/file/20220920",
                    "originalName": "2022-09-20-14-42-58-793.jpg",
                    "path": "/upload/file/20220920",
                    "purpose": "scsfz",
                    "size": 498154,
                    "uploadType": "file"
                }
            ],
            "bank": {
                "idCard": "D35633566444566666"
            },
            "base": {
                "birthday": "1998-01-01",
                "childNum": "0",
                "education": "1",
                "email": "fhjffhug@qq.com",
                "familyName": "vhj",
                "givenName": "chh",
                "idCardNum": "D35633566444566666",
                "instancyContacts": [
                    {
                        "contactName": "13wei02",
                        "contactPhone": "522190858525",
                        "contactRelation": "0",
                        "lastTime": 0
                    },
                    {
                        "contactName": "13wei01",
                        "contactPhone": "522187858625",
                        "contactRelation": "3",
                        "lastTime": 0
                    }
                ],
                "maritalStatus": "1",
                "middleName": "fhh",
                "placeAddress": "vhjjjj",
                "placeCity": "003002",
                "placeProvince": "003",
                "placeTime": "",
                "postalCode": "",
                "rfc": "",
                "sex": "2",
                "sysPlaceAddress": "",
                "uname": "",
                "whatsApp": "5806658668"
            },
            "configPayout": True,
            "customerSource": "com.mx.hinance",
            "firstExpectAmount": "1000.00",
            "firstExpectDay": "8",
            "livenessId": "",
            "merchantNo": "01",
            "orgNo": "MEX",
            "payoutPaymentConfig": {
                "bankConfig": {
                    "accountType": {
                        "label": "银行",
                        "value": "0"
                    },
                    "bankCard": "132500432406589999",
                    "bankType": {
                        "label": "NAFIN",
                        "value": "37135"
                    },
                    "name": "vhj chh fhh"
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
            "productNo": "MEX_01_1_20220617173142",
            "promotionChannels": "googlePlay",
            "sign": {
                "adbEnabled": 0,
                "androidId": "1f87332bd0b96267",
                "availableStorage": " 9.0563GB",
                "battery": "84",
                "codeName": "REL",
                "cpu": "armeabi-v7a",
                "cpuInfo": " MT6762G",
                "cpuSpeed": "1484000KHz",
                "currentWifi": "\"HAI-IT\"",
                "detailAddress": "",
                "deviceLanguage": "zh",
                "deviceMac": "94:17:00:7F:C7:F7",
                "deviceModel": "Xiaomi#M2006C3LG",
                "deviceSerial": "",
                "deviceSoftwareVersion": "78",
                "deviceVersionType": "user",
                "displayMetrics": "720,1449",
                "fingerPrint": "Redmi/dandelion_global/dandelion:10/QP1A.190711.020/V12.0.20.0.QCDMIXM:user/release"
                               "-keys",
                "gaid": "0c6b61b6-4604-422b-b264-121365738fea",
                "hardware": "mt6762",
                "imei": "",
                "imsi": "",
                "inDoor": -1,
                "lag": "",
                "lng": "",
                "locationAddress": "",
                "locationCity": "",
                "mobileName": "Redmi 9A",
                "model": "Xiaomi#M2006C3LG",
                "networkOperator": "",
                "networkOperatorName": "",
                "networkType": "wifi",
                "operatorName": "无服务,无服务",
                "os": "10",
                "phoneAvailableRam": " 0.6904GB",
                "phoneCardNum": "",
                "phoneOs": "Android",
                "phoneTotalRam": "MemTotal:        1819908 kB",
                "phonecardCount": 2,
                "product": "dandelion_global",
                "radioVersion": "MOLY.LR12A.R3.MP.V107.5.P125,MOLY.LR12A.R3.MP.V107.5.P125",
                "resolutionHeight": "1449",
                "resolutionWidth": "720",
                "rooted": 0,
                "routerMac": "f4:a4:d6:56:f9:90",
                "runtimeAvailableMemory": " 0.2361GB",
                "runtimeMaxMemory": " 0.2500GB",
                "simState": 1,
                "simulator": 0,
                "timeZone": "GMT+08:00",
                "totalStorage": " 22.6777GB",
                "turnOnTime": "2022-09-18 20:40:20",
                "uuid": "fa8e6c6474520d515b29198bb083a8014c47c44e15efd159358a4ce824c27573",
                "uuidOriginal": "[-6, -114, 108, 100, 116, 82, 13, 81, 91, 41, 25, -117, -80, -125, -88, 1, 76, 71, "
                                "-60, 78, 21, -17, -47, 89, 53, -118, 76, -24, 36, -62, 117, 115] "
            },
            "work": {
                "income": "1",
                "payDay": "15",
                "post": "0",
                "salaryType": "3",
                "secondPayDay": "",
                "sourceIncome": "0",
                "tel": "",
                "workTime": "0"
            }
        })
        try:
            response = Request('post', url_=url, body_=payload, headers_=self.headers, cookies=None).get_json()
        except Exception as e:
            Log().error("请求接口报错：{0}".format(e))
            raise e
        assert 0 == response["code"]
        assert "成功" == response["msg"]
        assert True is response["success"]
