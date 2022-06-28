# encoding: utf-8
import time

if __name__ == '__main__':
    from modules import *
else:
    from .modules import *
hour = (time.strftime("%H:%M", time.localtime()))

测试群 = 'https://oapi.dingtalk.com/robot/send?access_token=04fdda3277e1a65a54b7bd8e15f0d310607241801978ee4e6a2c1c2e0baeeba3'
正式群 = [
    #V3
    'https://oapi.dingtalk.com/robot/send?access_token=f2a21cf2221dd6424f71e77ea6037d91007a1bf7352c24c0bd402853ab03422b',
    #V2
    'https://oapi.dingtalk.com/robot/send?access_token=2ed80077a7f10f06c395d6573ab7399e8766a913c01994a24117d285c72ce9a1',
    #V1
    'https://oapi.dingtalk.com/robot/send?access_token=e665dca5c8142449e84a784e111d2d17b0e708595ed730a1646c0e19e625cc71',
    #OD
    'https://oapi.dingtalk.com/robot/send?access_token=83b92d8fc976f19f665add49748cb30324a870d98c57728248e69ed8099eda03'

]

 # 提醒兼职今天上班的老师，#每月1换！！
if str(hour) == '10:00': 
    for morning in worker.teacher()[0]: # 晚班提醒
        for i in 正式群:
            PushMobiles(i,
                        '今日督导',
                        '今天10:00-19:00上班的老师是:',
                        Mobiles=morning)

    for night in worker.teacher()[1]: # 晚班提醒
        for i in 正式群:
            PushMobiles(i,
                    '今日督导',
                    '今天14:00-22:00上班的老师是:',
                    Mobiles=night)
# 提醒交手机
if str(hour) == '18:50':
    worker.infos()   
