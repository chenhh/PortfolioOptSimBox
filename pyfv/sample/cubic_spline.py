# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
Cubic spline interpolation
http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
'''
__author__ = 'Hung-Hsin Chen'

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10)
y = np.cos(-x**2/8.0)

f = interp1d(x, y)  #linear
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, 40)
plt.plot(x,y,'o',xnew, f(xnew),'-', xnew, f2(xnew),'--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()

