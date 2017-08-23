import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd

try:
    data  = pd.read_excel(r"E:\PyCharm\Project\Numpy-Pandas\readData.xls", header=0)
    print data
except Exception,ex:
    print ex