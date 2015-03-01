# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
'''
__author__ = 'Hung-Hsin Chen'

#http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html

import numpy as np
import scipy.optimize as spopt

x0=np.random.randn()

def f(x):
    return x*x - 7*x + 10

print spopt.newton(f, x0)
