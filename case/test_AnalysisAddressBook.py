# 解析address_book_origin原始数据


from common.request_ import Request

url = '/hc/app/inner/unzlib'
data_ = "eNqlkTFPwzAQhf/KyQsSdMg1rs/uhjrAUKFKsCEGk55i08SWarcL4r+T" \
        "iA6JQQiJN949ve+d7vlddDblJ9+zWKOSqDURSl2Zheh8ODzYcSG23McAO0" \
        "7xKsHmlHLs+QiPfDz7hsWXdediGL2VMSustFI1DZtkz/xD+sdiDl6RMlTVy" \
        "uh6Br53rr3IDWpfXQt304l7cxcVNW60BENAqIEkoCy6TIBlF0UaqZYV" \
        "LtWsy3guNLE/Bb+3+wKHqAvCJOavhG1sbObuW7T5f/Rt5tD44YkWNp3nkDkVmGtE/IXz8gku/qSp"

t = Request('post', url_=url, body_=data_, headers_=None, cookies=None)
print(t.get_json())
