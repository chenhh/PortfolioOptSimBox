# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
'''
from django.db.backends.oracle.base import _UninitializedOperatorsDescriptor

__author__ = 'Hung-Hsin Chen'

import matplotlib.pyplot as plt
import numpy as np

def generate_data(params=None, n_pf=10000, n_observation=1000):
    '''
    :param params: parameters of SV model, (mu, phi, sigma2)
    :param n_pf: number of particle filter
    :param n_observation: number of observation
    :return:
    '''
    if params is None:
        mu =0.5
        phi = 0.975
        sigma2 = 0.04
        params = (mu, phi, sigma2)

    assert len(params) == 3

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

       #plot
    plt.title('stochastic volatility model')
    plt.plot(states, c="blue", label='state')
    plt.plot(observations, c="green", label='obs')
    plt.legend()
    plt.show()

    return {"states": states,
            "observations": observations}


def initialize_particle(params, n_pf):
    mu, phi, sigma2 = params
    particles = mu + np.sqrt(sigma2 / (1-phi)**2)*np.random.randn(n_pf)
    return particles


def SISR_PF_SV(n_pf=10000):
    #data generation
    mu =0.5
    phi = 0.975
    sigma2 = 0.04
    params = (mu, phi, sigma2)
    data =generate_data(params, n_pf=n_pf, n_observation=1000)
    states = data['states']
    observations = data['observations']
    n_observation = len(observations)

    #initialize particles
    particles = initialize_particle(params, n_pf)
    weights = np.ones(1, np.float)/n_pf
    likelihood = 0.

    for t in xrange(1, n_observation):
        #draw particles (samples)

        #estimate the next state (one-step ahead prediction)

        #compute importance weight

        #compute the log-likelihood

        #normalize weight

        #estimate current state (filtered)

        #compute ESS

        #resample and reset weight



if __name__ == '__main__':
    generate_data()