# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""

cdef class Stock:
    cdef float avg_price
    cdef int shares
    cdef readonly char* symbol

    # log format: (trans_date, symbol, price, share)
    trans_log = []

    def __cinit__(self, char* symbol):
        """
        called by Stock.__new__(symbol)
        """
        self.symbol = symbol
        self.avg_price = 0
        self.shares = 0

    def __init__(self, char* symbol):
        """
        called by Stock(symbol)
        """
        self.symbol = symbol
        self.avg_price = 0
        self.shares = 0

    def buy(self, trans_date, float price, int shares):
        pass

    def sell(self, trans_date, float price, int shares):
        pass


if __name__ == '__main__':
    a = Stock("hello")
    b = Stock.__new__("hello")