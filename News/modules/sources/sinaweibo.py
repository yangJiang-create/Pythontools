# encoding: utf-8
import requests
from bs4 import BeautifulSoup
from .base import Base

'''Sinaweibo搜获取类'''
class sinaweibo(Base):
    def __init__(self,logger_handle):
        super(sinaweibo, self).__init__(logger_handle)
        self.source = 'Sinaweibo'
        self.__initialize()

    def search(self):
        resp = requests.get(self.search_url,headers=self.headers)
        newSoup = BeautifulSoup(resp.text, "html.parser")
        titles = newSoup.find('div',id='pl_top_realtimehot')
        tille = titles.find_all('td',class_='td-02')

        title = [] 
        link = []
        for i in tille:
            real_title = i.find('a').text
            ul_link='https://s.weibo.com/weibo?q=%23{}%23&Refer=new_time'.format(real_title)
            title.append(real_title)
            link.append(ul_link)
        return zip(title,link)

    '''初始化'''
    def __initialize(self):
        self.headers = {
            'cookie':'SINAGLOBAL=7254774839451.836.1628626364688; SUB=_2AkMWR_ROf8NxqwJRmf8cymjraIt-ygDEieKgGwWVJRMxHRl-yT9jqmUgtRB6PcfaoQpx1lJ1uirGAtLgm7UgNIYfEEnw; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWEs5v92H1qMCCxQX.d-5iG; UOR=,,www.baidu.com; _s_tentry=-; Apache=1090953026415.7019.1632559647541; ULV=1632559647546:8:4:2:1090953026415.7019.1632559647541:1632110419050; WBStorage=6ff1c79b|undefined',
            'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'}
        self.search_url = 'https://s.weibo.com/top/summary?Refer=top_hot'