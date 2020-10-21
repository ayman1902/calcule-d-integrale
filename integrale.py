import numpy as np
import math as mt
import matplotlib.pyplot as plt
from pylab import *
# programmable by belhaj ayman
def f(x):
    return np.cos(x)
    
def calc(min,max,dx):
    '''min est la borne inf du fonction
       max est la borne sup du fonction
       dx est la precision  
       vous pouver changer la fct f(x)'''
    s = 0
    for i in np.arange(min,max,dx):
        s += dx*f(i)
    
    print(s)
    a = np.linspace(min,max,1000)
    plt.plot(a,f(a),label='f(x)')
    plt.title("area under this function is "+str(s))
    plt.axhline(color = 'k')
    fill_between(a, 0, f(a), color='blue', alpha=.25)
    plt.axvline(color = 'k')
    plt.legend()
    plt.show()

#calc(0,np.pi/2,0.0001)