# encoding: utf-8
import requests
from bs4 import BeautifulSoup
from .base import Base

'''Cctv热搜获取类'''
class cctv(Base):
    def __init__(self, logger_handle):
        super(cctv, self).__init__(logger_handle)
        self.source = 'cctv'
        self.__initialize()

    def search(self):
        resp = requests.get(self.search_url,headers=self.headers)
        resp.encoding = 'utf-8'
        newSoup = BeautifulSoup(resp.text, "html.parser")
        tiltle = newSoup.find('div',class_='boxTitle')

        title = [] 
        link = []
        for info in tiltle.find_all('a') :
                title.append(info.text)
                link.append(info['href'])
        return zip(title,link)

    '''初始化'''
    def __initialize(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        self.search_url = 'https://www.cctv.com/'