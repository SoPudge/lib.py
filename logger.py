#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

class Logger(object):
    def __init__(self,logger,**kw):
        '''
        creat a logger class,port from default loggin module
        Description:
            对于不传入**kw参数的调用，为旧式调用，用于一些旧式程序
            对于传输**kw的掉用，则支持如下功能
            1、定义日志的存储位置
            2、日志名称命名方式：以程序命名，以电脑命名
        '''
        #**kw参数定义
        if len(kw) == 0:
            #获取当前文件所在的目录
            file_path = sys.path[0]
            file_name = 'log.log'
        else:
            file_path = kw['file_path']
            file_name = kw['file_name']
        #**kw参数定义结束

        #creat a logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # creat a handler to output log to file
        self.fh = logging.FileHandler(file_path + '/' + file_name)
        self.fh.setLevel(logging.INFO)

        # creat a handler to output log to stream 
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)

        # formatter of log 
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)

        # add handler to logger
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def info(self,msg):
        self.logger.info(msg)

    def warning(self,msg):
        self.logger.warning(msg)

    def error(self,msg):
        self.logger.error(msg)

    def debug(self,msg):
        self.logger.debug(msg)

    def close(self):
        self.logger.removeHandler(self.fh)
        self.logger.removeHandler(self.ch)
        
if __name__ == '__main__':
    #kw = {'file_path':'N:\\005_Software','file_name':'abc.log'}
    logger = Logger('mylog')
    logger.info('this is in log')
