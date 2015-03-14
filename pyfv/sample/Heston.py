# -*- coding: utf-8 -*-
from math import *
from numpy import arange, array, zeros
from numpy.random import standard_normal

class HestonModel: 
    def __init__(self, num_steps, num_paths, s0, v0, r,theta, kappa, lamda, rho):
        self._num_steps = num_steps
        self._num_paths = num_paths
        #Initial stock price
        self._s0 = s0
        #Initial volatility
        self._v0 = v0
        #risk free rate
        self._r = r
        #long term volatility(equiribrium level)
        self._theta = theta
        #Mean reversion speed of volatility
        self._kappa = kappa
        #lambda(volatility of Volatility)
        self._lamda = lamda
        #rho
        self._rho = rho

    def _generate_path(self, dt):
        s = zeros(self._num_steps + 1)
        v = zeros(self._num_steps + 1)
        s[0] = self._s0            
        v[0] = self._v0
        dW1 = standard_normal(self._num_steps)
        dW2 = self._rho * dW1 + (1 - self._rho**2)**(0.5) * standard_normal(self._num_steps)
        for j in xrange(0, self._num_steps):
            s[j + 1] = s[j] * exp((self._r - 0.5 * v[j]) * dt + (v[j] * dt)**(0.5) * dW1[j])
            v[j + 1] = max(v[j] + (self._kappa * (self._theta - v[j]) * dt) + self._lamda * (v[j] * dt)**(0.5) * dW2[j], 0)
        return s            
    def price(self, option):
        payOff_Sum = 0.0
        for i in xrange(0, self._num_paths):
            payOff_Sum += option.payoff(self._generate_path(option.T / self._num_steps))
        return (exp(- self._r * option.T) * payOff_Sum / self._num_paths)


