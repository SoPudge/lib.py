#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pycurl
import certifi
from io import BytesIO 
from io import StringIO 
from urllib.parse import urlencode, quote_plus

class session(object):
    def __init__(self,proxies={},userpass=''):

        self.c = pycurl.Curl()
        #if no proxy,send data directly,or via proxy
        if len(proxies) != 0:
            self.c.setopt(self.c.PROXY, proxies['http'])
            self.c.setopt(self.c.PROXYUSERPWD, userpass)
            self.c.setopt(self.c.PROXYAUTH, self.c.HTTPAUTH_NTLM)
            self.c.setopt(self.c.CAINFO, certifi.where())
        self.c.setopt(self.c.CAINFO, certifi.where())
        self.c.setopt(self.c.VERBOSE,0)
        self.c.setopt(self.c.COOKIEJAR, 'cookie.txt')
        self.c.setopt(self.c.COOKIEFILE, 'cookie.txt')

    def get(self,url,isfile=False):
        '''
        '''
        buffers = BytesIO()
        self.c.setopt(self.c.URL,url)
        self.c.setopt(self.c.WRITEDATA, buffers)
        self.c.perform()
        if isfile == True:
            return buffers.getvalue()
        else:
            return buffers.getvalue().decode()

    def post(self,url,payload,ctype='',isfile=False):
        '''
        '''
        buffers = BytesIO()
        self.c.setopt(self.c.URL,url)
        self.c.setopt(self.c.WRITEDATA, buffers)
        if ctype == 'json':
            self.c.setopt(self.c.HTTPHEADER,['Content-Type: application/json; charset=utf-8'])
        elif ctype == 'xml':
            self.c.setopt(self.c.HTTPHEADER,['Content-Type: application/x-www-form-urlencoded; charset=utf-8'])
        else:
            self.c.setopt(self.c.HTTPHEADER,['Content-Type: application/x-www-form-urlencoded; charset=utf-8'])
            payload = urlencode(payload, quote_via=quote_plus)
        self.c.setopt(self.c.POSTFIELDS, payload)
        self.c.perform()
        if isfile == True:
            return buffers.getvalue()
        else:
            return buffers.getvalue().decode()

if __name__ == '__main__':
    proxies = {'http':'http://proxy.standard.corp:8080','https':'http://proxy.standard.corp:8080'}
    userpass = 'ls\\zhang180:#FCMZZQ890210'
    r = session(proxies,userpass) 
    m = r.get("http://www.baidu.com")
    print(m)
