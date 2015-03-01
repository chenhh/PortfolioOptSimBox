# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
The Nelder-Mead algorithm is a powerful and popular method to ﬁnd roots of multivariate functions.

'''
__author__ = 'Hung-Hsin Chen'

#http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html
import numpy as np
import scipy.optimize as spopt

def f(x):
    x,y = x
    return x*x-4*x+y*y-y-x*y

def g(x):
    x,y,z=x
    return (x-10)**2+(y+10)**2+(z-2)**2

fx0=np.array([10., 10.])
gx0=np.array([10., 10., 10.])

spopt.minimize(f, fx0, method='nelder-mead',
                options={'xtol': 1e-8, 'disp': True})

spopt.minimize(g, gx0, method='nelder-mead',
                options={'xtol': 1e-8, 'disp': True})