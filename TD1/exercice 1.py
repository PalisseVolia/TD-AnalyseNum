#Question 2:
n = int(input("donner n :"))
val = 1
for i in range(1,n+1):
    val = val + (1/(i+i**2))
print(val)