<<<<<<< HEAD
import requests
import pytest
import json


class Test_login:
    def test_01(self):
        url = "https://app.hinance.online/hc/app/noAuth/logon/login"

        payload = json.dumps({
            "promotionChannels": "googlePlay",
            "password": "",
            "flag": 1,
            "phone": "8888888881",
            "shortNo": "9999"
        })
        headers = {
            'app-name': 'Hinance',
            'app-version': '1.0.7',
            'channel': 'googlePlay',
            'commercialId': '01',
            'lang': 'zh',
            'organizationId': 'DCMEX',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload).json()

        expect = '成功'
        assert expect == response['msg']


if __name__ == '__main__':
    pytest.main(['-vs'])
=======
# import requests
# import pytest
# import json
#
#
# class Test_login:
#     def test_01(self):
#         # url = "https://app.hinance.online/hc/app/noAuth/logon/login"
#         url = ""
#
#         payload = json.dumps({
#             "promotionChannels": "googlePlay",
#             "password": "",
#             "flag": 1,
#             "phone": "8888888881",
#             "shortNo": "9999"
#         })
#         headers = {
#             'app-name': 'Hinance',
#             'app-version': '1.0.7',
#             'channel': 'googlePlay',
#             'commercialId': '01',
#             'lang': 'zh',
#             'organizationId': 'DCMEX',
#             'Content-Type': 'application/json'
#         }
#
#         response = requests.request("POST", url, headers=headers, data=payload).json()
#
#         expect = '成功'
#         assert expect == response['msg']
#
#
# if __name__ == '__main__':
#     pytest.main(['-vs'])
>>>>>>> 4decc10 (测试通过)
