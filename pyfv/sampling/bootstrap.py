# -*- coding: utf-8 -*-
'''
bootstrap methods

.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
'''


import numpy as np


def stationary_bootstrap(series, Q=0.5):
    '''
    **Dimitris N. Politis and Joseph P. Romano, "The stationary bootstrap,"
    Journal of the American Statistical Association, pp. 1303-1313, 1994.**

    :param series: if it is a 2d series, then the row index is model id and 
                   the  column index is time period.
    :type series: numpy.array

    :param Q: ir mean block size, if Q = 0.5, it means block size = 1/Q = 2.
    :type Q: float

    :return: random samples from series
    :rtype: numpy.array
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
