# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""
import numpy as np
import scipy.stats as spstats

_

def Black_Scholes(S, K, Tmt, r, sigma):
    """
    The value of a call option for a non-dividend-paying underlying stock

    Parameters:
    -----------------------------------------------
    S: spot price of the underlying asset
    K: strike price
    Tmt: time to maturity date (day)
    r: risk-free rate (continuous rate)
    sigma: (implied) volatility

    Return:
    -------------------------------
    return: current call and put option prices
    """
    #transform day to year
    T = Tmt/365.
    d1 = (np.log(S/K)+(r+sigma*sigma*0.5)*T)/(sigma * np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    cdf_d1, cdf_d2 = spstats.norm.cdf((d1, d2), loc=0, scale=1)

    discount_factor = K*np.exp(-r*T)
    call = cdf_d1 * S - cdf_d2*discount_factor
    put = discount_factor-S + call

    print "(S, K, T, r, sigma)=(%s, %s, %s, %s, %s)"%(S, K, T, r, sigma)
    print "call: %s, put: %s"%(call, put)
    return (call, put)


def test_Black_Scholes():
     Black_Scholes(S=9093., K=9000., Tmt=0.01, r=1.25/100, sigma=16.35/100)
    # Black_Scholes(S=100., K=95., Tmt=91, r=10/100., sigma=50/100.)


if __name__ == '__main__':
    test_Black_Scholes()