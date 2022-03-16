import numpy as np
import scipy.optimize as opt
#Question 1
#montrer par récurrence

#Question 2
def sigma(x):
    y = 20/(x**2+2*x+10)
    return y
x = 1
count = 0
alpha = 1.368808107
while np.abs(alpha - x) >= 10**-9:
    print(x)
    count = count + 1
    print(count)
    x = sigma(x)
#proche a 10^-10 quand n = 24
#valeur approchée : 1.3688081107179968

#Question 3
def fonction(x):
    y = x**3+2*x**2+10*x-20
    return y
a = 1           #début intervalle
b = 2           #fin intervalle
c = (a+b)/2     #milieu intervalle
while np.abs(alpha - c) >= 10**-9:
    if (fonction(a)*fonction(c)) < 0:
        b = c
        c = (a+b)/2
    elif (fonction(b)*fonction(c)) < 0:
        a = c
        c = (a+b)/2
print("le alpha est :")
print(c)

alpha = opt.fsolve(fonction, [1,2])
print("alpha via fsolve")
print(alpha)