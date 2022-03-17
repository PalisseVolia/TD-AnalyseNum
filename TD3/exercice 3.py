#%%
import matplotlib.pyplot as plt
import numpy as np

t = [0,10,20,30,40,50,60,70,80]
gom = [30,31.63,33.44,35.47,37.75,40.33,43.29,46.70,50.67]
plt.plot(t,gom)
def somme(tableau):
    n = len(tableau)
    s = 0
    for i in range(n):
        s = s + tableau[i]
    return s

print("Méthode des trapèzes:")
n = len(gom)
h = 10          #b-a/n soit la distance entre certains points

Itrapz = h*(0.5*(gom[0] + gom[n-1]) + somme(gom[1:n-1]))
print("Avec la méthode des trapèzes on trouve : ", Itrapz)

print()
print("Méthode de simpson:")

h = 20
Isimps = (h/6)*(gom[0] + gom[n-1] + 2*somme(gom[2:n-1:2]) + 4*somme(gom[1:n-1:2]))
print("Avec la méthode de simpson on trouve : ", Isimps)
# %%
