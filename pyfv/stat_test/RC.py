# -*- coding: utf-8 -*-
'''
Halbert White, “A REALITY CHECK FOR DATA SNOOPING,” Econometrica, 
Vol. 68, No. 5, pp. 1097-1126, 2000.

J. P. Romano and M. Wolf, “Stepwise multiple testing as formalized data 
snooping,” Econometrica, Vol . 73, pp. 1237–1282, 2005.

.. moduleauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
'''
from __future__ import division
from multiprocessing import Pool
import numpy as np


class DifferenceObject(object):
    '''difference series object for test '''
    
    def __init__(self, base_series):
        '''
        :param base_series: the benchmark series.
        :type base_series: numpy.array or list
        
        :var self.n_period: number of period
        "type self.n_period: int
        
        :var self.n_model: number of model to comparison
        :type self.n_model: int
        
        :var self.model_series_mtx: model series mtx for comparison
        :type self.model_series_mtx: 2d numpy.array
        '''
        base_series = np.asarray(base_series)
        self.base_series = base_series
        self.n_period = base_series.size
        self.n_model = 0
        self.model_series_mtx = None

    def set_model_series(self, model_series):
        '''
        :param model_series: the model series for comparison.
        :type model_series: numpy.array or list
        '''
        model_series = np.asarray(model_series)
        
        if model_series.size != self.n_period:
            raise ValueError("model series:%s unequal to base:%s"%(
                    model_series.size, self.n_period))
        
        if self.model_series_mtx is None:  
            self.model_series_mtx =  model_series
        else: 
            self.model_series_mtx = np.vstack((
                                    self.model_series_mtx, 
                                    model_series ))
        self.n_rule += 1
        
    def difference_mtx(self):
        '''
        :return: difference matrix between each model and base series 
        :rtype: 2d numpy.array
        
        user can override this function for their differnece function
        '''
        diff_mtx = self.model_series_mtx - self.base_series
        return diff_mtx


def RC_test():
    pass

def stepwise_RC_test():
    pass

if __name__ == '__main__':
    pass