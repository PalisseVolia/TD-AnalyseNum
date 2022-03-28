#%%
import math
import matplotlib.pyplot as plt
import numpy as np

print()
#Question 1
print("Question 1:")
print()

#intégrale de f : e^x de 0 à 1 = e-1

print()
#Question 2
print("Question 2:")
print()

a = 0
b = 1
integ = math.exp(1)-1
somme = 0
n = int(input("donner n :"))
tabptmil = list()
tabtrapz = list()
tabsimps = list()

#méthode points milieux
#estimation
def ptmil(a,b,n):
    h = (b-a)/n
    I = 0
    for i in range(n):
        I = I + math.exp(a+i*h)
    I = h*I
    return(I)
def Trapz(a,b,n) :
    h = (b - a)/n
    I = 0.5 *(math.exp(a) + math.exp(b))
    for i in range(1,n) :
        I = I + math.exp(a + i*h)
    I = h*I
    return I
def Simps(a,b,n) :
    h = (b-a)/n
    I = math.exp(a) + math.exp(b) + 4*math.exp(a + h/2)
    for i in range(1,n) :
        I = I + 2*math.exp(a + i*h) + 4*math.exp(a + h/2 + i*h)
    I = (h/6)*I
    return I

for k in range(1, n):
    tabptmil.append(np.abs(integ - ptmil(a,b,k)))
    tabsimps.append(np.abs(integ - Trapz(a,b,k)))
    tabtrapz.append(np.abs(integ - Simps(a,b,k)))

def plaute():
    x = [k for k in range(1, n)]
    plt.plot(np.log(x),np.log(tabptmil),color='r')
    plt.plot(np.log(x),np.log(tabsimps),color='g')
    plt.plot(np.log(x),np.log(tabtrapz),color='b')
    plt.show()
plaute()

print(Simps(a,b,n))


        
#     for k in range(n):
#         somme = somme + math.exp((c+d)/2)
#         c = d
#         d = d + b/n
#     return (((b-a)/n)*somme)
# print(mn(n,a,b,c,d))
# %%
