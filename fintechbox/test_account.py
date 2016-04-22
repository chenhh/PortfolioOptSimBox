# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""
from account import Stock

def test_Stock():
    a = Stock("hello")
    b = Stock.__new__(Stock, "hello")


if __name__ == '__main__':
    test_Stock()