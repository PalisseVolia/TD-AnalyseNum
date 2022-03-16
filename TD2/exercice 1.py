import numpy as np

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
print(x)
count = count + 1
print(count)
x = sigma(x)
#proche a 10^-10 quand n = 25
#valeur approchée : 1.368808106535769

#Question 3
a = 1       #début intervalle
b = 2       #fin intervalle
c = 1.5     #milieu intervalle