# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
'''
__author__ = 'Hung-Hsin Chen'

import numpy as np
import scipy.misc as spmisc
import scipy.stats as spstats
import matplotlib.pyplot as plt
import scipy.optimize as spopt

def CRRbinomial(S, K, T, rf, sigma, n):
    '''
    Option pricing using binomial tree, no dividend
    :param S: underlying current prince
    :param K: option strke price
    :param T: expire date
    :param rf: risk-free rate
    :param sigma: volatility
    :param n: number of periods to T
    :return:
    '''
    dt = float(T)/n
    u = np.exp(sigma * (dt**0.5))
    d= 1./u
    p = (np.exp(rf*dt)-d)/(u-d)

    euroCall, euroPut = 0, 0

    for idx in xrange(0, n+1):
        euroCall += spmisc.comb(n, idx)* (p**idx) * (1-p)**(n-idx)*np.max((S*(u**idx)*(d**(n-idx))-K, 0))
        euroPut += spmisc.comb(n, idx)* (p**idx) * (1-p)**(n-idx)*np.max((K-S*(u**idx)*(d**(n-idx)), 0))

    euroCall *= np.exp(-rf*T)
    euroPut *= np.exp(-rf*T)
    return euroCall, euroPut


def BlackScholes(S, K, T, rf, sigma):
    '''
    without dividend
    put-call parity
    C-P = S - K*e^(-rT)

    :param S:
    :param K:
    :param T:
    :param rf:
    :param sigma:
    :return:
    '''
    sqrtT = np.sqrt(T)
    dc = K*np.exp(-rf*T)
    d = (np.log(S/K)+T*(rf+0.5*sigma*sigma))/(sigma*sqrtT)
    put = dc*spstats.norm.cdf(sigma*sqrtT-d)-S*spstats.norm.cdf(-d)
    call = S - dc+put
    return call, put


def impliedVolatility(S, K, T, rf, optionValue, optionType='call'):
    '''
    given Call or put, S, K, T, rf,
    return: corresponding sigma
    '''
    if optionType == "call":
        val = 0
    elif optionType == 'put':
        val =1
    else:
        raise ValueError("unknown optionType: %s"%(optionType))

    def f(x):
        return (optionValue - BlackScholes(S, K, T, rf, x)[val])**2
    x0 = 1.0
    root = spopt.newton(f, x0)
    return root

print CRRbinomial(S=30, K=30, T=0.4167, rf=0.05, sigma=0.3, n=500)
print BlackScholes(S=30, K=30, T=0.4167, rf=0.05, sigma=0.3)
print impliedVolatility(S=100, K=100, T=0.3753, rf=0.03, optionValue=15.0676)