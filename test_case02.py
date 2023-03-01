import requests
import pytest


def reqHttp(url, data, headers):
    res = requests.post(url, data, headers)
    return res.json()


class Test_login:
    def test_01(self):
        url = "http://192.168.122.176:9010/hc/app/noAuth/logon/doRegister"
        data = {"promotionChannels": "googlePlay",
                "password": "",
                "flag": "01",
                "phone": "2221591217",
                "countryCode": "52",
                "shortNo": "9999"}
        header = {
            'app-name': 'Hinance',
            'app-version': '1.0.7',
            'channel': 'googlePlay',
            'commercialId': "1",
            'lang': 'zh',
            'organizationId': 'DCMEX',
            'token': '',
            'Content-Type': 'application/json'
        }
        res = reqHttp(url, data, header)

        expect = '成功'
        assert expect == res['msg']


if __name__ == '__main__':
    pytest.main()
