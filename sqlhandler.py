#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import uuid
import _mssql
import decimal
import pymssql
from logger import Logger
decimal.__version__
uuid.ctypes.__version__
_mssql.__version__

logger = Logger('ms_sql_handler')
class SqlHandler(object):
    '''
    get formated data from a mssql server db,input connect details,return a list[dict1,dict2...]
    return data is just list&formated,easy to use,may be not use for sending directly.
    '''
    def __init__(self):
        pass
    def get_data(self,server,username,password,dbname,query):
        '''
        this func get data from mssql,format this data as dict, and return it,
        mssql connect details must be configured in config.ini[DB],
        data from mssql is unformated and contain a lot of spaces,so i creat a loop
        formating data,also re-store it in a list[dcit1,dict2...],finnaly return it.

        Args:
            connect details,all str,example as below
            SERVER = 10.166.49.31\CNWUTWIT0001
            USERNAME = Mii_db_r
            PASSWORD = faurecia1
            DBNAME = MII_db
            QUERY = SQL Query
            CODEC = charset determined by source mssql,normally utf8 or cp936

        Returns:
            return a formated&list data from mssql
        ''' 

        conn = pymssql.connect(server,username,password,dbname)
        cursor = conn.cursor(as_dict=True)
        cursor.execute(query)
        data = cursor.fetchall()

        for x in data:
            for k,v in x.items():
                try:
                    x[k] = str(v).replace(' ','').encode('latin-1').decode('gbk')
                except:
                    x[k] = str(v).replace(' ','')
        cursor.close()
        if len(data) == 0:
            logger.info('no data from sql,no sending')
        else:
            logger.info('read data from sql OK')
        return data

    def insert_data(self,server,username,password,dbname,query,data):
        """
        This method insert values into db
        Args:
            connect details,all str,example as below
            SERVER = 10.166.49.31\CNWUTWIT0001
            USERNAME = Mii_db_r
            PASSWORD = faurecia1
            DBNAME = MII_db
            QUERY = SQL Query
            DATA = date you want to insert,as executemany method,data format normally
            [(),(),()]

        Returns:None
        """
        conn = pymssql.connect(server,username,password,dbname)
        cursor = conn.cursor()
        cursor.executemany(query,data)
        try:
            conn.commit()
            logger.info('insert data from sql OK')
        except:
            logger.warning('insert error, please check the query')

    def del_data(self,server,username,password,dbname,query):
        """
        This method delete data from db
        Args:
            connect details,all str,example as below
            SERVER = 10.166.49.31\CNWUTWIT0001
            USERNAME = Mii_db_r
            PASSWORD = faurecia1
            DBNAME = MII_db
            QUERY = SQL Query

        Returns:None
        """
        conn = pymssql.connect(server,username,password,dbname)
        cursor = conn.cursor()
        cursor.execute(query)
        try:
            conn.commit()
            logger.info('delete data from sql OK')
        except:
            logger.warning('delete error, please check the query')

if __name__ == '__main__':
    #This section is test case for sending data via proxy
    query = "SELECT kittingOrderCode,partdesc,line,station,material,boxqty,pdastatus FROM View_kitting_order_detail_toDD"
    query2 = "SELECT * FROM View_sis_pm_repair_request_equipment_wc_toDD"
    query3 = "SELECT * FROM View_alert_list_plc_open_toDD"
    query4 = "SELECT * FROM View_alert_list_plc_open_toDD_delay"
    query5 = "SELECT GAPDescription,CreatedDate,CreatedBy,Problem,Cause,Action,Resp,DeadLine,UAPDescription FROM View_actionsplans_masters_overdue WHERE UAPDescription='JiangXia Plant'"
    query6 = "SELECT ALERT_ID,ALERT_CODE,PLANT,ALERT_LEVEL,CREATED_TIMESTAMP,ALERT_DETAILS,PART,UAP,PROD_LINE,WORKCENTER,date,PARTS_DESCRIPTION FROM View_alert_list_open_compshort_toDD"
    query7 = "INSERT INTO alert_cs_stock_list (alert_mii_id,alert_mii_date,alert_mii_plant,alert_mii_mtl,alert_mii_loc,alert_mii_qty,alert_mii_comm) VALUES ('1','2018-05-14 03:47:02.000','1038','test','IN10','100','TEST')"
    query8 = "SELECT ALERT_ID,PLANT,PART,alert_date,alert_cs_time FROM View_alert_list_open_query_stoc"
    query9 = "SELECT ALERT_ID,PLANT,PART,alert_date FROM View_alert_list_open_query_close"
    query10 = """INSERT INTO [NON_TRS_TICKET_SPLIT] ([PLANT] ,[TICKET] ,[STATUS] ,[CAUSE] ,[DURATION] ,[CAUSE_1] ,[CAUSE_2] ,[EQUIPMENT] ,[REMARK] VALUES ('1038', '10008', 'CLSD', '2', '0:14:00', '201', '', 'E160067', '')"""
    ftesSql = SqlHandler()
    #data = ftesSql.get_data('10.166.49.31\CNWUTWIT0001','Mii_db_r','faurecia1','MII_db',query8)
    data = ftesSql.insert_data('10.166.49.31\CNWUTWIT0001','Mii_db_rw','faurecia1','MII_db',query10)
    #data = ftesSql.get_data('10.166.49.31\CNWUTWIT0001','Mii_db_r','faurecia1','E_Leveing_PQ',query)
    #data = ftesSql.get_data('10.166.49.31\CNWUTWIT0001','Mii_db_r','faurecia1','eTOP5',query5)
    #kittingOrderCode_all = list(set([i['kittingOrderCode'] for i in data]))
    #print(etop5)
    #for i in data:
    #    print(i)
