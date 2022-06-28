# encoding: utf-8
import requests
import json


def PushMobiles(url, keyword, texts, all=False, Mobiles='', img=''):
    url = url  # 设置机器人的地址
    pagrem = {
        "msgtype": "markdown",
        "markdown": {
            "title": f"{keyword}",
            "text": f'''#### {keyword}
                            \n >{texts}
                            @{Mobiles}
                            {img}
                            '''
        },
        "at": {
            "atMobiles": [
                f"{Mobiles}"
            ],
            "isAtAll": all
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.post(url, data=json.dumps(pagrem), headers=headers)
    return res.json()

