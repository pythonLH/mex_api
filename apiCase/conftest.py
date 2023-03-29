import requests
import json
import pytest
from apiMethod.common.config_ import red_
from apiMethod.ospath.ConfigurePaths import database_dir


@pytest.fixture(scope="class", autouse=False)
def class_fixture_login():
    # 这个登录接口前端先写死后面，后面直接引用配置文件
    url = "https://app.hinance.online/hc/app/noAuth/logon/login"

    payload = json.dumps({
        "promotionChannels": "googlePlay",
        "password": "",
        "flag": "1",
        "phone": "6666666661",
        "shortNo": "3927"
    })

    headers = {
        'app-name': 'Hinance',
        'app-version': '1.0.7',
        'channel': 'googlePlay',
        'commercialId': '01',
        'lang': 'zh',
        'organizationId': 'DCMEX',
        'token': '',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=payload).json()

    # 接口依赖，下个接口调用，需要用到的东西
    return response["data"]["token"]




