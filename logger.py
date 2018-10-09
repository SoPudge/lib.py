#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import logging

class Logger(object):
    def __init__(self,logger):
        """ 
        creat a logger class,port from default loggin module
        """
        #creat a logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # creat a handler to output log to file
        log_name = 'log.log'
        fh = logging.FileHandler(sys.path[0] + '/' + log_name)
        fh.setLevel(logging.INFO)

        # creat a handler to output log to stream 
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # formatter of log 
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add handler to logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

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
        
if __name__ == '__main__':
    logger = Logger('mylog')
    logger.info('this is in log')
