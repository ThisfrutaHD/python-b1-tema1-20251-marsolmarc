"""
Enunciat:

Implementa una funció anomenada find_max(lst) que trobi el valor màxim en una
llista de números utilitzant recursió. La funció ha de tornar el valor
màxim de la llista.

Paràmetres:
     lst (List): llista de nombres enters o flotants

Exemple:
     Entrada:
     numbers_list = [1, 5, 2, 7, 3]
     fid_max(numbers_list)

     Sortida:
     7

"""


def find_max(lst):
    if len(lst) == 1: #Cas Base
        return lst[0]
    else:
        return max(lst[0], find_max(lst[1:]))


# Si vols provar el teu codi, descomenta les línies següents i executa l'script
numbers_list = [1, 5, 2, 7, 3, 25]
print(find_max(numbers_list))