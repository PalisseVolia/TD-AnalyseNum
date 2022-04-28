#%%
import math
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
    # resultat = EulerValue(t,y)
    # return resultat
    return y,t

# class EulerValue:
#     def __init__(self,t,y):
#         self.t = t
#         self.y = y

print()
print("Question 2:")
print()

def f1(t,y):
    return -y
def f2(t,y):
    return -(y**2)

print()
print("Question 3:")
print()

y0 = 1
