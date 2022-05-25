#%%
print()
print("Question 1:")
print()

import math
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as alg

n = 10;
COND = []
N = []
for i in range(1,n+1):
    AN = np.diag(np.ones(i),0)*2-np.diag(np.ones(i-1),1)-np.diag(np.ones(i-1),-1)
    COND.append(np.linalg.cond(AN))
    N.append(i)
print(COND)
print(N)
plt.plot(N,COND)

#%%
print()
print("Question 2:")
print()

import math
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as alg

n = 500;
AN = np.diag(np.ones(n),0)*2-np.diag(np.ones(n-1),1)-np.diag(np.ones(n-1),-1)
cond = np.linalg.cond(AN)
def condnum(n):
    return (4/(np.pi**2))*n**2

ERROR = []
N = []
for i in range(1,n+1):
    AN = np.diag(np.ones(i),0)*2-np.diag(np.ones(i-1),1)-np.diag(np.ones(i-1),-1)
    cond = np.linalg.cond(AN)
    ERROR.append(abs((condnum(i)-cond)/condnum(i)))
    N.append(i)
    
plt.plot(N,ERROR)