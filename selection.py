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

def selection(liste):
  i =0
  for i in range(len(liste[i:])):
    indice_plus_petit = minimum(liste[i:])
    liste[i], liste[indice_plus_petit+i] = liste[indice_plus_petit+i], liste[i]
  return liste


print(selection(liste))
