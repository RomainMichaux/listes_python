from random import *

liste = []
for i in range(20):
  x = randint(0, 20)
  liste.append(x)
print(liste)

def insertion(liste):
  print(liste)
  liste_triee = []
  liste_triee.append(liste[0])
  for element in liste[1:]:
    print('---------------------------------------')
    print(f'Element a tester : {element}')
    dernier = len(liste_triee)-1
    print(liste_triee)
    print(f'Position du dernier : {dernier}')
    i=dernier
    while i>=0 and element < liste_triee[i]:
      print(f'Pas en {i+1}')
      i-=1
    print(f'Placer en  {i+1}')
    liste_triee.insert(i+1,element)
    print(f' {liste_triee}')   
  return liste_triee

insertion(liste)
