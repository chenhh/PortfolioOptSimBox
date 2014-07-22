# -*- coding: utf-8 -*-
'''
@author: Hung-Hsin Chen
phase space reconstruction
'''
import pandas as pd
import numpy as np
from time import time
import scipy.spatial.distance as spdist
import matplotlib.pyplot as plt
import rpy2.robjects as ro
from rpy2.robjects.numpy2ri import numpy2ri

#import R package
R_tseriesChaos = ro.packages.importr('tseriesChaos')
R_fNonlinear = ro.packages.importr('fNonlinear')
R_nonlinearTseries = ro.packages.importr('nonlinearTseries')


def reconstruction(series, tau, m):
    '''
    :series: pandas.Series
    :tau: positive integer, delayed index
    :m: postive integer, dimension of phase space
        
    return
    :df: pandas.Dataframe, reconstructed time series
    '''
    if tau <= 0 or m <= 0 or not isinstance(series, pd.Series):
        raise ValueError
    
    df = pd.DataFrame(series, columns=['t',])
    
    if m == 1:
        return df
    
    for d in xrange(m-1):
        idx = (d+1)*tau
        df['tm%d'%idx] = series.shift(idx)
 
    return df[idx:]


def R_reconstruction(series, tau, m):
    '''
    http://cran.r-project.org/web/packages/tseriesChaos/tseriesChaos.pdf
    embedd(x, m, d, lags)
    '''
    res =  R_tseriesChaos.embedd(numpy2ri(series), m, tau)
    print type(res), np.asmatrix(res)

def correlationIntegral(df, r, metric="inf"):
    '''
    df: pandas.DataFrame, reconstructed data
    r: positive float number, threshold value

    spdist.pdist will compute pairwise distance of the row in the mtx
    http://en.wikipedia.org/wiki/Correlation_integral
    '''
    if metric == 'inf':
        metric = lambda u, v: np.max(abs(u-v))
    elif metric == 'euclidean':
        metric = 'euclidean'
    
    n_data, _ = df.shape    
    dists = r - spdist.pdist(df.as_matrix(), metric=metric)
    counter = (dists >= 0).sum()
    return 2. * counter / (n_data * (n_data - 1))


def R_correlationIntegral(series, tau, m, t, r):
    '''
    http://cran.r-project.org/web/packages/tseriesChaos/tseriesChaos.pdf
    
    C2(series, m, d, t, eps)
    series: time series
    m: embedding dimension
    d: time delay
    t: Theiler window
    eps: length scale
    '''
    res =  R_tseriesChaos.C2(numpy2ri(series), m, tau, t, r)
    print res[0]


def R_falseNeighbor(series, tau, m):
    '''
    http://cran.r-project.org/web/packages/tseriesChaos/tseriesChaos.pdf
    '''
    print R_tseriesChaos.false_nearest(numpy2ri(series), m, tau, 10)

def testReconstruction():
    series = pd.Series(np.random.randn(20), index=range(20))
    print series
    t = time()
    print reconstruction(series, tau=2, m=5)
    t1 = time()
    print R_reconstruction(series, tau=2, m=5)
    t2 = time()
    print "orig:", t1-t, "secs"
    print "R:", t2-t1, "secs"
#     print disjointSeries(series, tau=4)
#     R_falseNeighbor(series, tau=2, m=5)

def testCorrelationIntegral():
    series = pd.Series(np.random.randn(100), index=range(100))
    df = reconstruction(series, tau=2, m=3)
    std = series.std()
    print correlationIntegral(df, std)
    print correlationIntegral(df, std, 'euclidean') 



if __name__ == '__main__':
    testReconstruction()
#     testCorrelationIntegral()
