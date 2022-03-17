import numpy as np
import scipy.optimize as opt
import math
#Question 1
#montrer par récurrence

#Question 2
print("Question 2:")
print()

def sigma(x):
    y = 20/(x**2+2*x+10)
    return y
x = 1
count = 0
n = math.floor(np.log(10**-10)*np.log(0.5))+1           #n pour précision à 10^-10 près
for i in range(n):
    x = sigma(x)
print("Pour n = ", n)
print("On a alpha =", x)

print()
#Question 3
print("Question 3:")
print()

def fonction(x):
    y = x**3+2*x**2+10*x-20
    return y
a = 1           #début intervalle
b = 2           #fin intervalle
c = (a+b)/2     #milieu intervalle
n = math.floor(np.log((b-a)/10**-16)/np.log(2)) + 1     #n dichotomie pour précision à 10^-16 près soit précision machine
for i in range(n):
    if (fonction(a)*fonction(c)) < 0:
        b = c
        c = (a+b)/2
    else:
        a = c
        c = (a+b)/2

print("dichotomie:")
print("Pour n = ", n)
print("On a alpha =", c)
print()

print("fsolve:")
alpha = opt.fsolve(fonction, [1,2])
print("On a alpha =", alpha)

print()
#Question 4
print("Question 4:")
print()

#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def sigma(x):
    y = 20/(x**2+2*x+10)
    return y
n = 20
erreur = np.zeros(n)        #tableau de taille n rempli de 0
x0 = 1
xn = 0
alpha = 1.368808107
erreur[0] = np.abs(x0-alpha)
for i in range(1, n):
    xn = sigma(xn)
    erreur[i] = np.abs(xn-alpha)
x = [k for k in range(n)]
plt.plot(x,np.log(erreur))
# %%
