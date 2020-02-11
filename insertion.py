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

def insertion(liste):
  liste_triee = []
  print(liste)
  j = 0
  for element in liste:
    liste_triee.append(element)
    print(liste_triee)
    i=0

    while (i+2)>= 0 and j>0 and liste_triee[-1-i] < liste_triee[-2-i]:
      liste_triee[-1-i],liste_triee[-2-i] = liste_triee[-2-i], liste_triee[-1-i]
      print(f'{j} , {i} : {liste_triee}')
      i+=1
    j+=1   
  return liste_triee

#print(selection(liste))
insertion(liste)