import requests
import json
import pytest
from apiMethod.common.config_ import red_
from apiMethod.ospath.ConfigurePaths import database_dir


@pytest.fixture(scope="class", autouse=False)
def class_fixture_login():
    # 这个登录接口前端先写死后面，后面直接引用配置文件
    url = "http://192.168.122.239:7037/hc/app/noAuth/logon/login"

    payload = json.dumps({
        "promotionChannels": red_(database_dir).red_get('login_data', 'promotionChannels'),
        "password": red_(database_dir).red_get('login_data', 'password'),
        "flag": red_(database_dir).red_get('login_data', 'flag'),
        "phone": red_(database_dir).red_get('login_data', 'phone'),
        "shortNo": red_(database_dir).red_get('login_data', 'shortNo')
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
