from random import *

liste = []
for i in range(20):
  x = randint(0, 20)
  liste.append(x)
print(liste)

def minimum(liste):
  minimum = liste[0]
  indice = indice_mini = 0
  for element in liste:
    if element < minimum:
      minimum = element
      indice_mini = indice
    indice+=1
  return indice_mini

print(minimum(liste))

indice_plus_petit = minimum(liste)
liste[0], liste[indice_plus_petit] = liste[indice_plus_petit], liste[0]


print(liste)
