# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
x(t) = mu + phi * (x(t-1) - mu) + sigma * eta(t)
z(t) = exp(x(t)/2)*epsilon(t)

'''

__author__ = 'Hung-Hsin Chen'

import matplotlib.pyplot as plt
import numpy as np

def generate_data(params=None, n_particle=10000, n_observation=1000):
    '''
    :param params: parameters of SV model, (mu, phi, sigma2)
    :param n_particle: number of particle filter
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


def initialize_particle(params, n_particle):
    '''
    初始化particle之值
    :param params: (mu, phi, sigma2) of SV
    :param n_particle: number of particle
    '''
    mu, phi, sigma2 = params
    particles = mu + np.sqrt(sigma2 / (1-phi)**2)*np.random.randn(n_particle)
    return particles


def importanceSampling(params, particles, n_particle):
    '''
    importance density is the transition density
    x(t) = mu + phi * (x(t-1) - mu) + sigma * eta(t)
    所以particle之值代表state的樣本，而非observation的樣本
    '''
    mu, phi, sigma2 = params
    particles = mu + phi*(particles - mu) + np.sqrt(sigma2)*np.random.randn(
        n_particle)
    return particles


def logIncrementalImportanceWeights(dY, particles):
    '''
    incremental update importance weight
    '''
    weights = -0.5*np.log(2*np.pi) - 0.5*particles - 0.5*(1./np.exp(
        particles))*dY**2

    return weights


def SISR_PF_SV(n_particle=10000):
    #data generation
    mu =0.5
    phi = 0.975
    sigma2 = 0.04
    params = (mu, phi, sigma2)
    data =generate_data(params, n_particle=n_particle, n_observation=1000)
    states = data['states']
    observations = data['observations']
    n_observation = len(observations)
    predictions = np.zeros(n_observation)

    #initialize particles
    particles = initialize_particle(params, n_particle)
    weights = np.ones(1, np.float)/n_particle
    likelihood = 0.

    for t in xrange(1, n_observation):
        #draw new particles (samples)
        particles = importanceSampling(params, particles, n_particle)

        #estimate the next state (one-step ahead prediction)
        #期望值(積分)等於particles(value) * weights (probability)
        predictions[t] = np.sum(particles * weights)

        #compute importance weight

        #compute the log-likelihood

        #normalize weight

        #estimate current state (filtered)

        #compute ESS

        #resample and reset weight
        pass



if __name__ == '__main__':
    generate_data()