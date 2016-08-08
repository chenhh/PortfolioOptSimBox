# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""

import numpy as np
import pandas as pd

def Sharpe(series, rf=0., unbiased=True):
    """
    Sharpe ratio
    note that the numpy std() function is the population estimator

    Parameters:
    -----------
    series: list or numpy.array
        return of investment series
    rf: float
        return of risk free asset
    unbiased: bool
        unbiased estimator of standard deviation or not

    Return:
    -------
    float
        Sharpe ratio of the given series.

        if the standard deviation of the series is 0, return 0.
    """
    s = np.asarray(series)
    if unbiased:
        var = s.var(ddof=1)
        std = np.sqrt(var)
    else:
        std = s.std()
    try:
        val = (s-rf).mean() / std
    except FloatingPointError:
        # set 0 when standard deviation is zero
        val = 0
    return val


def Sortino_full(series, mar=0):
    """
    Sortino ratio, using all periods of the series

    Parameters:
    ---------------
    series: list or numpy.array, ROI series
    mar: float, minimum acceptable return, usually set to 0
    """
    s = np.asarray(series)
    mean = s.mean()
    semi_std = np.sqrt(((s * ((s - mar) < 0)) ** 2).mean())
    try:
        val = mean / semi_std
    except FloatingPointError:
         # set 0 when semi-standard deviation is zero
        val = 0
    return val, semi_std


def Sortino_partial(series, mar=0):
    """
    Sortino ratio, using only negative roi periods of the series

    Parameters:
    ---------------
    series: list or numpy.array, ROI series
    mar: float, minimum acceptable return, usually set to 0
    """
    s = np.asarray(series)
    mean = s.mean()
    n_neg_period = ((s - mar) < 0).astype(np.int).sum()
    try:
        semi_std = np.sqrt(((s * ((s - mar) < 0)) ** 2).sum() / n_neg_period)
        val = mean / semi_std
    except FloatingPointError:
        # set 0 when semi-standard deviation or negative period is zero
        val, semi_std = 0, 0
    return val, semi_std


def maximum_drawdown(series):
    """
    https://en.wikipedia.org/wiki/Drawdown_(economics)
    the peak may be zero
    e.g.
    s= [0, -0.4, -0.2, 0.2]
    peak = [0, 0, 0, 0.2]
    therefore we don't provide relative percentage of mdd

    Parameters:
    ---------------
    series: list or numpy.array, ROI series
    """
    s = np.asarray(series)
    peak = pd.expanding_max(s)

    # absolute drawdown
    ad = np.maximum(peak - s, 0)
    mad = np.max(ad)

    return mad