import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
from collections import OrderedDict
from pyexcel_xls import get_data

try:
    # date_index = pd.date_range('20170824',periods=6)
    #
    # data = pd.DataFrame(pd.arange(),index=date_index,columns=list('ABCD'))

    # for item, in data.iterrows():
        # print item
    # print data.shape[0]
    # print data

    data = np.arange(20)
    print data
except Exception,ex:
    print ex