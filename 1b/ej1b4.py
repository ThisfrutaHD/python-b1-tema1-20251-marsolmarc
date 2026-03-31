'''
Enunciat:

Implementar la funció 'results(list_numbers)' que rebi com a paràmetre una
llista que conté nombres enters i decimals anomenada 'list_numbers', es demana
calcular la mitjana i la desviació estàndard mitjançant la
llibreria "Numpy" de tots els números dins de la llista.

Cada resultat s'ha d'imprimir en pantalla amb el nom respectiu
'Average: {value}' i 'Standard deviation: {value}', aquests resultats deuen
estar arrodonits a 2 decimals.

Els resultats també han de ser retornats per la funció.

Pots consultar la referència de la llibreria 'Numpy' en el següent enllaç:
https://numpy.org/doc/stable/reference/index.html#reference

En concret, et recomanem que consultis:
* https://numpy.org/doc/stable/reference/generated/numpy.mean.html
* https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std

Paràmetre:
- list_numbers: Llista de nombres enters i decimals.

Exemple:
     Entrada:
     [1, 2, 10, -5, 0, 9.55, 74.825, 55, 8, 42]
    
     Sortida:
     Average: 19.74
     Standard deviation: 26.03
'''


import numpy as np

def results(list_numbers):
    mitjana = np.mean(list_numbers)
    desviacio = np.std(list_numbers)
    print("Mitjana: ", round(mitjana, 2))
    print("Desviacio estandard: ", round(desviacio, 2))
    return mitjana, desviacio

# Si vols provar el teu codi, descomenta les línies següents i executa l'script
results([1, 2, 10, -5, 0, 9.55, 74.825, 55, 8, 42])