# encoding: utf-8
import time
import threading
import logging
import os

if __name__ == '__main__':
    from modules import *
    from __init__ import __version__
else:
    from .modules import *
    from .__init__ import __version__


class News():
    def __init__(self):
        self.logger_handle = './news.log'
        logging.basicConfig(filename=self.logger_handle, level=logging.INFO)
        self.initializeAllSources()

    '''run'''

    def run(self):
        Now = time.strftime('%H:%M')
        LogoTime = time.strftime('%H:%M:%S')
        for mail in NewAccept:
            if Now == NewAccept[mail]:
                # 跑提取数据的代码
                data = download.getdownload(self, mail)
                logging.info(f'{LogoTime}数据导出成功')
                # 生成词云
                wordcloud_path = getcouldword.getcouldword(self, data)
                logging.info(f'{LogoTime}词云生成成功')
                # 添加发送账号
                sendmail.sendmail(
                    self, Newsender, mail[0], data, wordcloud_path)
                logging.info(f'{LogoTime}邮件发送成功')
        if Now in TimeList:
            for key, values in self.search(NewsSources).items():
                download.download(self, key, values)
                logging.info(f'{LogoTime}数据下载成功')

    '''新闻搜索'''

    def search(self, target_srcs):
        def threadSearch(search_api, target_src, search_results):
            try:
                search_results.update({target_src: search_api()})
            except Exception as err:
                logging.error(str(err), True)
                logging.warning(f'无法在{target_src}中搜索...')

        task_pool, search_results = [], {}

        for target_src in target_srcs:
            task = threading.Thread(
                target=threadSearch,
                args=(getattr(self, target_src).search, target_src, search_results))

            task_pool.append(task)
            task.start()

        for task in task_pool:
            task.join()

        return search_results

    '''初始化所有支持的源'''

    def initializeAllSources(self):
        supported_sources = {
            'bilibli': bilibili,
            'cctv': cctv,
            'chinadaily': chinadaily,
            'sinaweibo': sinaweibo
        }
        for key, value in supported_sources.items():
            setattr(self, key, value(self.logger_handle))


if __name__ == '__main__':
    # 信息源
    NewsSources = ('bilibli', 'cctv', 'sinaweibo', 'chinadaily')

    # 更新数据时间
    TimeList = ('05:00', '00:00')

    # 发件人*（填的是邮箱账户+授权码）
    Newsender = ('*********@foxmail.com', '*********')

    # 收件人*（冒号不要写错）
    '''(邮箱号、每类信息的条数（1-10）、信息源（默认四种）):接收时间 '''
    NewAccept = {('*********@qq.com', 5, NewsSources): '06:00',
                 ('*********@qq.com', 5, NewsSources): '08:00',
                 ('*********@qq.com', 5, NewsSources): '08:30',
                 }

    # 实例化+运行
    dl_client = News()

    # Linux
    dl_client.run()
    # 若为windows系统，可以在此处设置while True:
    # while True:
    #    dl_client.run()
