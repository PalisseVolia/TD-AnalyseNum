#%%
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

print()
print("Question 1:")
print()

def Euler(f, T, y0, n):
    h = T/n
    y = [y0]
    t = [0]
    for i in range(n):
        y.append(y[i] + h*f(t[i],y[i]))
        t.append(t[i] + h)
    return y

def yderiv(t,y):
    return 3*y-3*t

T = 20
a = 1/3
b = 0.333
n = 1000

t1 = np.linspace(0,T,n+1)

resultat = Euler(yderiv,T,a,n)
plt.plot(t1,resultat,color='r')

resultat = Euler(yderiv,T,b,n)
plt.plot(t1,resultat,color='g')

#CCL : les graphes obtenus par y0=1/3 et y0=0.333 sont très éloignés. On veut savoir pourquoi
    
# %%

print()
print("Question 2:")
print()

#petit a

#résoluton de l'équation différentielle y'=3y-3t avec y(0)=1/3
#On commence par la solution homogène y'=3y : Sh = Ke^(3t)
#On fait ensuite la solution particulière y'=3y-3t : Sp = t + 1/3
#Par conséquent la solution de l'équa diff est : S = Sh + Sp = Ke^(3t) + t + 1/3 = t + 1/3 avec y(0)=1/3

#petit b

#On prend y(0)=1/3+eps alors y(t) = 1/3 + eps*e^3t + t
#Donc pour T T grand meme si eps petit les solutions seront très éloignées
#Exemple avec eps = 10^-10 et T = 20 : y(t) = 1/3 + 10^-10*e^3t + 20 = 1.14e16
