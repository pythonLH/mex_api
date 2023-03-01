import requests
import pytest


def reqHttp(url, data, headers):
    res = requests.post(url, data, headers)
    return res.json()


class Test_login:
    def test_01(self):
        url = "https://app.hinance.online/hc/app/noAuth/logon/login"
        data = {
            "promotionChannels": "googlePlay",
            "password": "",
            "flag": 1,
            "phone": "8888888881",
            "shortNo": "9999"
        }
        header = {
            'app-name': 'Hinance',
            'app-version': '1.0.7',
            'channel': 'googlePlay',
            'commercialId': '01',
            'lang': 'zh',
            'organizationId': 'DCMEX',
            'Content-Type': 'application/json'
        }
        res = reqHttp(url, data, header)
        print(res)

        expect = '成功'
        assert expect == res['msg']


if __name__ == '__main__':
    pytest.main()
