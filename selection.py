from random import *

liste = []
for i in range(20):
  x = randint(0, 20)
  liste.append(x)
print(liste)

minimum = liste[0]
indice = indice_mini = 0
for element in liste:
  if element < minimum:
    minimum = element
    indice_mini = indice
  indice+=1
print(indice_mini, minimum)

liste[0], liste[indice_mini] = liste[indice_mini], liste[0]

print(liste)