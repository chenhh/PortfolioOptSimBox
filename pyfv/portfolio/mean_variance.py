# -*- coding: utf-8 -*-
'''
@author: Hung-Hsin Chen
@mail: chenhh@par.cse.nsysu.edu.tw

Markowitz mean variance model
'''

from __future__ import division
from coopr.pyomo import *
from time import time
from datetime import date
import numpy as np
import pandas as pd
import os
import time
from coopr.opt import  SolverFactory


def MeanVariance(symbols, risk_ret, money=1e6, risk_weight=1, solver="cplex"):
    '''
    @riskyRet, shape: M*T
    minimize risk_weight * risk  - (1-risk_weight) * mean
    '''
    t = time.time()
    
    sigma = np.cov(risk_ret)
    mu = risk_ret.mean(axis=1)
    
    model = ConcreteModel()
    
    #Set
    model.symbols = range(len(symbols))
       
    #decision variables
    model.W = Var(model.symbols, within=NonNegativeReals)
    
    #constraint
    def CapitalConstraint_rule(model):
        allocation = sum(model.W[idx] for idx in model.symbols)
        return allocation == money
    
    model.CapitalConstraint = Constraint()

    #objective
    def minRiskObjective_rule(model):
        profit = sum(model.W[idx]*mu[idx] for idx in model.symbols)
        risk = 0
        for idx in model.symbols:
            for jdx in model.symbols:
                    risk += model.W[idx] * model.W[jdx] * sigma[idx, jdx]
        
        return 1./2 * risk_weight * risk - (1. - risk_weight) * profit
        
    model.minRiskObjective = Objective(sense=minimize)
    
    # Create a solver
    opt = SolverFactory(solver)
    
    if solver =="cplex":
        opt.options["threads"] = 4
    
    instance = model.create()
    results = opt.solve(instance)  
    instance.load(results)
    obj = results.Solution.Objective.__default_objective__['value']
    display(instance)
    
    print "MeanVariance elapsed %.3f secs"%(time.time()-t)


def testMeanVariance():
    FileDir = os.path.abspath(os.path.curdir)
    PklBasicFeaturesDir = os.path.join(FileDir, '..', 'pkl', 'BasicFeatures')
    
    symbols = ['2330', '2317', '6505']
    n_period = 100
    ROIs = np.empty((len(symbols), n_period))
    for idx, symbol in enumerate(symbols):
        df = pd.read_pickle(os.path.join(PklBasicFeaturesDir, '%s.pkl'%symbol))
        roi =  df['adjROI'][:n_period]
        ROIs[idx] = roi
        
    MeanVariance(symbols, ROIs, money=1e6, risk_weight=1, solver="cplex")

if __name__ == '__main__':
    testMeanVariance()