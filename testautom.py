#%%

import math
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

w = 0
n = 400

def Gain(w):
    gains = 20*np.log10(20/(np.sqrt(((4*w**2)+1)*(100+w**2))))
    return gains
def Argument(w):
    Args = -np.arctan(2*w)-np.arctan(w/10)
    return Args

tabgain = []
tabarg = []

for i in range(n):
    tabgain.append(Gain(w))
    tabarg.append(Argument(w))
    w = w + 0.1
# plt.axis(0, n,)
plt.plot(tabarg,tabgain)

print(Argument(0.2))
# %%
