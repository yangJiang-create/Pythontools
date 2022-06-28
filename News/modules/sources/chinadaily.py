# encoding: utf-8
import requests
from bs4 import BeautifulSoup
from .base import Base

'''chinadaily搜获取类'''
class chinadaily(Base):
    def __init__(self,logger_handle):
        super(chinadaily, self).__init__(logger_handle)
        self.source = 'chinadaily'
        self.__initialize()

    def search(self):
        resp = requests.get (self.search_url,headers=self.headers,timeout=10)
        newSoup = BeautifulSoup(resp.text, "html.parser")
        titles = newSoup.find('div',class_='content_left')
        tille = titles.find_all('div',class_='gy_box')
        
        title = [] 
        link = []
        for i in tille:
            info = i.find('p',class_='gy_box_txt2')
            ul_link=info.find('a')['href'].replace(' ', '')
            real_title = info.find('a').text
            title.append(real_title)
            link.append('http:'+ul_link)
        return zip(title,link)

    '''初始化'''
    def __initialize(self):
        self.headers = {'cookie':"_uuid=A4F09FB6-DA12-D846-C77D-F27E110329A012910infoc; buvid3=5B53EDC5-884E-44CE-9564-85224AE2811C167633infoc; b_nut=1627706613; fingerprint=a4cee378a67596eddb4e2de85720fe9d; buvid_fp=5B53EDC5-884E-44CE-9564-85224AE2811C167633infoc; buvid_fp_plain=5B53EDC5-884E-44CE-9564-85224AE2811C167633infoc; SESSDATA=366d4142%2C1643258742%2Cdb703%2A71; bili_jct=e575bfd6537397c709b4a0a79cfdbcf8; DedeUserID=333411352; DedeUserID__ckMd5=17440a6007f05b38; sid=jfq479jh; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k||lYRmJ~R0J'uYk~~|Y~Y|; CURRENT_BLACKGAP=1; CURRENT_QUALITY=0; bp_video_offset_333411352=553683565784675075; bp_t_offset_333411352=553911241997013898; PVID=1",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        self.search_url = 'http://language.chinadaily.com.cn/thelatest'