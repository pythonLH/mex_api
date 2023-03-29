import requests
import json
import pytest
from apiMethod.common.config_ import red_
from apiMethod.ospath.ConfigurePaths import database_dir


@pytest.fixture(scope="class", autouse=False)
def class_fixture_login():
    # 这个接口前端先写死后面，直接引用配置文件
    url = "http://192.168.122.239:7037/hc/app/noAuth/logon/login"

    payload = json.dumps({
        "promotionChannels": "googlePlay",
        "password": "",
        "flag": 1,
        "phone": "1586599999",
        "shortNo": "9999"
    })
    headers = {
        'app-name': red_(database_dir).red_get('headers', 'app-name'),
        'app-version': red_(database_dir).red_get('headers', 'app-version'),
        'channel': red_(database_dir).red_get('headers', 'channel'),
        'commercialId': red_(database_dir).red_get('headers', 'commercialId'),
        'lang': red_(database_dir).red_get('headers', 'lang'),
        'organizationId': red_(database_dir).red_get('headers', 'organizationId'),
        'token': red_(database_dir).red_get('headers', 'token'),
        'Content-Type': red_(database_dir).red_get('headers', 'Content-Type')
    }

    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=payload).json()
    # 接口依赖，下个接口调用，需要用到的东西
    return response["data"]["token"]
