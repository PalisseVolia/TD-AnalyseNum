import math
import matplotlib.pyplot as plt
import matplotlib as mpl

#%%
#Question 1
s1 = math.exp(-10)
print(s1)

#Question 2
n = int(input("donner n :"))
tabsuite = list()
s2 = 0
def uk(k):
    uk = (10**k)/math.factorial(k)
    return uk
for i in range(0,n+1):
    tabsuite.append(uk(i))
    print("Le terme de rang ", i, " est ", tabsuite[i])
x=[k for k in range(n+1)]
plt.plot(x,tabsuite)
plt.show

#Question 3
n = int(input("donner n :"))
for i in range(0,n+1):
    s2 = s2 + ((-1)**i)*uk(i)
print("(", s1, "  :  ", s2, ")")