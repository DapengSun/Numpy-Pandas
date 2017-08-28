# -*- coding: utf-8 -*-
import re
import urllib2
import sys
import MySQLdb
import time
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
        Sql = self.GetDataSql % str(Date)
        df = pd.read_sql(Sql, db, index_col="ID")

        df[['HousePrice']] = df[['HousePrice']].astype('int32')
        print df.groupby(['HouseArea'])[['HousePrice']].mean()
        # return df


    def LocalDate(self):
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))

_analysis = Analysis()
LocalDate = _analysis.LocalDate()
_analysis.GetHomeLinkData(LocalDate)


