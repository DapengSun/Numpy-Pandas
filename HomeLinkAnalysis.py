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
        self.GetDataSql = 'Select * from HouseInfo Where Date(CDate) = "%s"'

    def GetHomeLinkData(self,Date):
        try:
            Sql = self.GetDataSql % str(Date)
            df = pd.read_sql(Sql, db, index_col="ID")

            # df[['HousePrice']] = df[['HousePrice']].astype('int32')

            # HousePrice = df[['HousePrice']].head(3)
            # HouseArea = df[['HouseArea']].head(3)

            HousePrice = ('10000')
            HouseArea = ('西苑')

            bar_width = 0.35
            index = np.arange(1)

            rects1 = plt.bar(0,HousePrice[0],bar_width,color='#0072BC', label=HouseArea[0])
            # rects2 = plt.bar(index + bar_width, HousePrice[1], bar_width, color='#0072BC', label=HouseArea[1])
            # rects3 = plt.bar(index + bar_width + bar_width, HousePrice[2], bar_width, color='#ADFF2F', label=HouseArea[2])

            plt.xticks(index + bar_width, HouseArea)
            plt.ylim(ymax=200000, ymin=0)# Y轴范围
            plt.title(u'HomeLink')  # 图表标题
            plt.show()

        except Exception,ex:
            print ex
        # plt.
        # plt.ylim(ymax=100, ymin=0)  # Y轴范围
        #
        # plt.title(u'HomeLink')  # 图表标题
        # plt.show()
        # print df.groupby(['HouseArea'])[['HousePrice']].mean()
        # df.groupby(['HouseArea'])[['HouseArea','HousePrice']].max().to_excel("abc.xls",sheet_name="123",index=False,header=True)
        # return df
        # print df.groupby(['HouseArea'])[['HousePrice']].max()
        # print df[['HouseArea','HousePrice']].max()
        # 极差
        # Range = df['HousePrice'].max() - df['HousePrice'].min()
        # 组距
        # GroupLen = 10000
        # 组数
        # GroupNum = Range / GroupLen
        # print GroupNum

    def LocalDate(self):
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))

_analysis = Analysis()
LocalDate = _analysis.LocalDate()
_analysis.GetHomeLinkData(LocalDate)


