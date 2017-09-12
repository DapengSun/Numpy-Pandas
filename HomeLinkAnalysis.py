# -*- coding: utf-8 -*-
import re
import urllib2
import sys
import MySQLdb
import time
import openpyxl
import xlwt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
reload(sys)
sys.setdefaultencoding( "utf-8" )

db = MySQLdb.connect("localhost", "root", "sdmp", "spiderdb",charset='utf8')

class Analysis:
    def __init__(self):
        # self.cursor = db.cursor()
<<<<<<< Updated upstream
        self.GetDataSql = 'Select HouseName,HouseTotalPrice,HousePrice from HouseInfo'
    #     ,HousePattern,HouseRange,HousePace,HouseStyle,

    def GetHomeLinkData(self):
        try:
            # Sql = self.GetDataSql
            # df = pd.read_sql(Sql, db)
            # start = time.time()
            # df['HouseTotalPrice'] = df['HouseTotalPrice'].astype(float)
            # grouped = df['HouseTotalPrice'].groupby(df['HouseName']).mean()
            # end = time.time()
            # grouped.to_excel('foo.xlsx', sheet_name='Sheet1')
            # print end - start

            start = time.time()
            print 'start'
            reader = pd.read_csv(r'E:\PyCharm\Project\HouseInfo.csv', iterator=True,error_bad_lines=False)
            loop = True
            chunkSize = 10000000
            chunks = []
            while loop:
                try:
                    chunk = reader.get_chunk(chunkSize)
                    chunks.append(chunk)
                except StopIteration:
                    loop = False
                    print "Iteration is stopped."
            df = pd.concat(chunks, ignore_index=True)

            df['HouseTotalPrice'] = df['HouseTotalPrice'].astype(float)
            grouped = df['HouseTotalPrice'].groupby(df['HouseName']).mean()

            end = time.time()
            grouped.to_excel('foo.xlsx', sheet_name='Sheet1')

            print 'end'
            print end - start
        except Exception,ex:
            print ex
=======
        self.GetDataSql = 'Select * from HouseInfo Where Date(CDate) = "%s"'

    def GetHomeLinkData(self,Date):
        Sql = self.GetDataSql % str(Date)
        df = pd.read_sql(Sql, db, index_col="ID")

        df[['HousePrice']] = df[['HousePrice']].astype('int32')
        # print df.groupby(['HouseArea'])[['HousePrice']].mean()
        # df.groupby(['HouseArea'])[['HouseArea','HousePrice']].max().to_excel("abc.xls",sheet_name="123",index=False,header=True)
        # return df
        # print df.groupby(['HouseArea'])[['HousePrice']].max()
        # print df[['HouseArea','HousePrice']].max()
        # 极差
        # print df['HousePrice'].max() - df['HousePrice'].min()
        # 组距
        # GroupLen = 10000
        # # 组数
        # GroupNum = Range / GroupLen
        # print GroupNum

    def LocalDate(self):
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))
>>>>>>> Stashed changes

_analysis = Analysis()
_analysis.GetHomeLinkData()


