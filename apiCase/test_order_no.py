import json

import pytest

from apiMethod.common.request_ import Request


class Test_OrderNo:

    def test_01(self, class_fixture):
        url = "/hc/app/loan/queryAvailableProduct"

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
        token_ = class_fixture
        headers = {
            'app-name': 'Hinance',
            'app-version': '1.0.7',
            'channel': 'googlePlay',
            'commercialId': '1',
            'lang': 'zh',
            'organizationId': 'DCMEX',
            'token': token_,
            'Content-Type': 'application/json'
        }

        response = Request('post', url_=url,
                           body_=payload,
                           headers_=headers,
                           ).get_json()

        assert "成功" == response["msg"]


if __name__ == '__main__':
    pytest.main(['-v'])
