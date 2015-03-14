# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
stochastic volatility
'''
__author__ = 'Hung-Hsin Chen'


def Heston93(v0, S0, T, r, vbar, kappa, vlambda, rho, n):
    '''
    :param v0: initial volatility level
    :param S0: spot price
    :param T: maturity of options (in years)
    :param r: riskfree rate
    :param vbar: long term volatility
    :param kappa: mean reversion speed of volatility
    :param vlambda: volatility of volatility
    :param rho: correlation
    :param n: steps
    :return:
    '''
    dt = float(T)/n

