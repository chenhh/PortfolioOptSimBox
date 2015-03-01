# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
'''
__author__ = 'Hung-Hsin Chen'

import numpy as np

#\int_1^2 e^x dx
def f(x):
    # return np.exp(x)
    return x**3+10

def leftPointIntegral(f, slice=100, a=1, b=2):
    x=np.linspace(a , b, slice)
    integral =0
    for idx in xrange(1, len(x)):
        dX = x[idx]-x[idx-1]
        integral += dX * f(x[idx-1])
    return integral

def rightPointIntegral(f, slice=100, a=1, b=2):
    x=np.linspace(a , b, slice)
    integral =0
    for idx in xrange(1,len(x)):
        dX = x[idx]-x[idx-1]
        integral += dX * f(x[idx])
    return integral


def TrapezoidalIntegral(f, slice=100, a=1, b=2):
    x=np.linspace(a , b, slice)
    integral =0
    for idx in xrange(1, len(x)):
        dX = x[idx]-x[idx-1]
        integral += 0.5 * dX * (f(x[idx])+f(x[idx-1]))
    return integral


def SimpsonIntegral(f, slice=100, a=1, b=2):
    x=np.linspace(a , b, slice)
    integral =0
    for idx in xrange(2, len(x), 2):
        dX = x[idx]-x[idx-1]
        integral += 1/3.*(f(x[idx]) + 4*f(x[idx-1])+ f(x[idx-2])) * dX

    return integral


def Simpson38Integral(f, slice=100, a=1, b=2):
    x=np.linspace(a , b, slice)
    integral =0
    for idx in xrange(3, len(x), 3):
        dX = x[idx]-x[idx-1]
        integral += 3/8.*(f(x[idx])+3*f(x[idx-1])+3*f(x[idx-2])+f(x[idx-3]))*dX
    return integral

def BooleIntegral(f, slice=100, a=1, b=2):
    x=np.linspace(a , b, slice)
    integral =0
    for idx in xrange(4, len(x), 4):
        dX = x[idx]-x[idx-1]
        integral += dX/45.*(14*f(x[idx])+64*f(x[idx-1])+24*f(x[idx-2])+64*f(x[idx-3])+14*f(x[idx-4]))
    return integral


print "left:", leftPointIntegral(f, 1000)
print "right:", rightPointIntegral(f, 1000)
print "Trapezoidal:", TrapezoidalIntegral(f, 1000)
print "Simpson:", SimpsonIntegral(f,1001)
print "Simpson38:", Simpson38Integral(f,1000)
print "Boole:", BooleIntegral(f, 1000)

import scipy.integrate as spint
print "quad:", spint.quad(f, 1,2)
print "fixed_quad:", spint.fixed_quad(f,1,2)
print "quadrature:", spint.quadrature(f,1,2)
print "romberg:", spint.romberg(f,1,2)