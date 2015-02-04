# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
'''
__author__ = 'Hung-Hsin Chen'
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as spstats
import pandas as pd
import os
# csvfile = os.path.join('e:', 'TAIEX_2.csv')
# data = pd.read_csv(csvfile)
# rets = data['return']

rets = pd.Series(np.random.randn(10000))
# plt.hist(rets, bins=30)
plt.title("Simulation")
plt.xlabel("Value")
plt.ylabel('count')
rets.hist(bins=30, )
print "mean:", rets.mean()
print "stdev", rets.std()
print "skewness", spstats.skew(rets)
print "kurtosis", spstats.kurtosis(rets)
print spstats.jarque_bera(rets)
plt.show()


print "hello world"