# -*- coding: utf-8 -*-
"""
Author: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
"""

cdef class Stock:
    """
    The class represents the current holding stock in the portfolio

    Attributes:
    -----------
    symbol: string
        the symbol name of the stock
    ave_price: float
        the current market price of the stock
    shares: int
        the current holding shares of the stock


    """
    cdef readonly char* symbol
    cdef float avg_price
    cdef int shares


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