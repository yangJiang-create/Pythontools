# encoding: utf-8
import requests
import bs4

'''信息搜集器基类'''
class Base():
    def __init__(self,logger_handle):
        self.source = None
        self.logger_handle = logger_handle
    '''搜索'''
    def search(self):
        raise NotImplementedError('not be implemented...')
    '''初始化'''
    def __initialize(self):
        raise NotImplementedError('not be implemented...')
    '''返回类信息'''
    def __repr__(self):
        return 'News Source: %s' % self.source