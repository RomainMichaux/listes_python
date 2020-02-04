from random import *

liste = []
for i in range(20):
  x = randint(0, 20)
  liste.append(x)
print(liste)

maximum = liste[0]
for element in liste:
  if element > maximum:
    maximum = element
print(maximum)
 