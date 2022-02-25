#Question 1:
n = int(input("donner n :"))
st = 2-(1/(n+1))
print(st)

#Question 2:
#petit nombre ajouté au grand (erreur élevée)
sr = 1
for i in range(1,n+1):
    sr = sr + (1/(i+i**2))
print(sr)
print("L'erreur relative méthode 1 est :")
err = abs(st-sr)/abs(st)
print(err)

#grand nombre ajouté au petit (erreur faible)
sr = 0
for i in range(n,0,-1):
    sr = sr + (1/(i+i**2))
sr = sr + 1
print(sr)
print("L'erreur relative méthode 2 est :")
err = abs(st-sr)/abs(st)
print(err)