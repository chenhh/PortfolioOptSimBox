# -*- coding: utf-8 -*-
'''
:author: Hung-Hsin Chen

Politis, Dimitris N., and Joseph P. Romano. "The stationary bootstrap." 
Journal of the American Statistical Association 89.428 (1994): 1303-1313.
'''
import numpy as np


def stationary_bootstrap(series, Q=0.5):
    '''
    :series, numpy.array, if it is 2-d series, then the row index is model id 
              and the column index is time period
    :Q, float, mean block size
    if Q = 0.5 then mean block size = 1/Q = 2
    '''
    # validation
    series = np.asarray(series)
    if series.ndim == 1:
        n_period = series.shape[0]
    elif series.ndim == 2:
        n_period = series.shape[1]
    else:
        raise ValueError('wrong dimension of series,dim:%s' % (series.ndim))

    colidx = np.zeros(n_period, dtype=np.int)
    colidx[0] = np.random.randint(0, n_period)

    for t in xrange(1, n_period):
        u = np.random.rand()
        if u < Q:
            colidx[t] = np.random.randint(0, n_period)
        else:
            colidx[t] = colidx[t - 1] + 1
            if colidx[t] >= n_period:
                colidx[t] = 0

    if series.ndim == 1:
        samples = series[colidx]
    elif series.ndim == 2:
        samples = series[:, colidx]

    return  samples


if __name__ == '__main__':
    pass
