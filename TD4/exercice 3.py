#%%
import math
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

print()
print("Question 1:")
print()

#Déterminons la solution de l'équa diff y' = -150y+30 avec y0 = alpha
#On commence par la solution homogène y'= -150y : Sh = Ke^(-150t)
#On fait ensuite la solution particulière y'= -150y+30 : Sp = 1/5
#Par conséquent la solution de l'équa diff est : S = Sh + Sp = Ke^(-150t) + 1/5 = Ke^(-150t) + 1/5 avec y(0)=alpha

