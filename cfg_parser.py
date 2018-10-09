#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import configparser

class CfgParser(object):
    '''
    CfgParser for read config.ini file.
    read all data from config.ini and restore it in a dict
    example:
        {GLOBAL:{},DB:{}....}
    '''
    def __init__(self):
        pass

    def get_user_cfg(self):
        content = {}
        subcontent = {}
        config = configparser.ConfigParser()
        config.read('config.ini')
        sections = config.sections()
        for section in sections:
            for i in config[section]:
                subcontent[i] = config[section][i]
            content[section] = subcontent
            subcontent = {}
        return content

if __name__ == '__main__':
    #This section is test case for reading ini file
    config = CfgParser()
    UAP = config.get_user_cfg() 
    server = UAP['UAP1']['template_ntrs']
    UAP.pop('GLOBAL')
    UAP.pop('DB')
    joblist = UAP
    print(joblist)
    #test

    #for k,v in UAP.items():
    #    print(k)
