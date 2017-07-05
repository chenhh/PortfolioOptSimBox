#!/usr/bin/env python
"""
https://github.com/cython/cython/wiki/InstallingOnWindows
https://github.com/cython/cython/wiki/CythonExtensionsOnWindows

go to start menu >
    Microsoft Visual C++ Compiler Package for Python 2.7 >
    Visual C++ 2008 64-bit Command Prompt

Enter the following commands:
    SET DISTUTILS_USE_SDK=1
    SET MSSdk=1

You can then "cd X:yourpath" to navigate to your Python app and then
build your C extensions by entering:
     python setup.py build_ext --inplace --compiler=msvc

the MSVC compiler default optimization level: /Ox (Full Optimization)
https://msdn.microsoft.com/en-us/library/59a3b321.aspx

"""
try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension


from Cython.Build import cythonize
import numpy as np
import os

extensions = [
    Extension(
        "benchmark",
        ["fintechbox/benchmark.pyx",],
        include_dirs = [np.get_include()],
    ),
    Extension(
        "account",
        ["fintechbox/account.pyx", ],
        include_dirs=[np.get_include()],
    ),

]

setup(
    name = 'PortfolioOptSimBox',
    description='portfolio optimization simulation toolbox',
    author = 'Hung-Hsin Chen',
    author_email = 'chenhh@par.cse.nsysu.edu.tw',
    ext_modules = cythonize(extensions),
)
