# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
'''
from gst._gst import object_set_control_rate

__author__ = 'Hung-Hsin Chen'

import matplotlib.pyplot as plt
import numpy as np

def generate_data(n_pf=10000, n_observation=1000):
    '''
    :param params: parameters of SV model, (mu, phi, sigma2)
    :param n_pf: number of particle filter
    :param n_observation: number of observation
    :return:
    '''
    mu =0.5
    phi = 0.975
    sigma2 = 0.04
    params = (mu, phi, sigma2)

    #observation noise
    eta = np.random.randn(n_observation+100)

    #process noise
    eps = np.random.randn(n_observation)

    #system state
    states = np.zeros(n_observation + 100)

    states[0] = np.random.rand()
    for t in xrange(1, n_observation + 100):
        states[t] = mu + phi * (states[t-1] - mu) + np.sqrt(sigma2)*eta[t]

    states = states[100:]

    #observation
    observations = np.exp(states/2.) * eps

    print len(states)
    print len(observations)

    plt.title('stochastic volatility model')
    plt.plot(states)
    plt.plot(observations)
    plt.show()


if __name__ == '__main__':
    generate_data()