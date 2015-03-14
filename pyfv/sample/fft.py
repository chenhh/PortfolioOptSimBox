# -*- coding: utf-8 -*-
'''
.. codeauthor:: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
'''
__author__ = 'Hung-Hsin Chen'

import numpy as np
f= np.arange(1, 9)
h =np.fft.fft(f)
print (abs(f)**2).sum() #204
print (abs(h)**2).mean()    #204

h2 = np.fft.fft(-f)
print "h2: ", h2
print h.conjugate()

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)


fig, ax = plt.subplots()
ax.set_title('time domain')
ax.plot(x,y)

fig, ax = plt.subplots()
ax.set_title("frequency domain")
ax.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
plt.show()