import sympy as smp
import numpy as np
import matplotlib.pyplot as plt


from sympy import assoc_laguerre

r, a = smp.symbols('r a', real=True, positive=True)
n, l = smp.symbols('n l', integer=True, positive=True)

R = smp.sqrt((2/(n*a))**3*smp.factorial(n-l-1)/(2*n*(smp.factorial(n+1))))*smp.exp(-r/(n*a))*(2*r/(n*a))**l*assoc_laguerre(n-l-1, 2*l+1, (2*r/(n*a)))

################
##############"
#############
