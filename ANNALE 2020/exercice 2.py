#%%
import math
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as alg
N = 10;
DX = 1/(N+1)

AN = np.diag(np.ones(N),0)*2-np.diag(np.ones(N-1),1)-np.diag(np.ones(N-1),-1)
print(AN)
print()
BN = np.diag(np.ones(N-1),1)-np.diag(np.ones(N),0)
print(BN)
print()
CN = np.zeros((N,N))
CN[(N-1,N-1)] = -2/(DX**2*(2+DX))+4/(DX*(DX+2))
print(CN)
print()
MN = np.zeros((N,N))
MN = (1/DX**2)*AN+(2/DX)*BN+CN
print(MN)
print()
RHS = -np.ones((N,1))
RHS[(0,0)] = (1/DX**2)-1
RHS[(N-1,0)] = 2/(DX*(DX+2))-4/(DX+2)-1
print(RHS)
print()
YN = alg.solve(MN,RHS)
print(YN)

# %%
