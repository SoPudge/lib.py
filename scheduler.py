#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import time
import threading
from logger import Logger

logger = Logger('scheduler')
class Scheduler(object):
    def __init__(self):
        pass

    #def time_parse(self):
    #    case_fixed = bool(sche_method == 'fixed' and sche_time == now_time_hour)
    #    case_interval = bool(sche_method == 'interval' and int(now_time_min)%int(sche_time) == 0)

    def sche_job(self,job):
        while True:
            time.sleep(1)
            now_time = time.strftime("%S", time.localtime())
            #every minutes 20 seconds
            if now_time == '20':
                t = threading.Thread(target=job, name='LoopThread')
                t.start()
            else:
                continue
            logger.info('\r\n')

if __name__ == '__main__':
    s = Scheduler()
    #every-return class ,at return class,do
    #s.every(1,sec/min/hour/day).at('08:00').do('job')
    #s.every(1,sec/min/hour/day).do('job')
    pass
