'''
Enunciat:
Crea una funció 'sum_odd_numbers(list_numbers)' que rebi com
paràmetre una llista de nombres positius enters anomenada 'list_numbers'
i torneu la suma dels números imparells trobats a la llista.
Considereu que 'list_numbers' ha de contenir valors numèrics enters majors
o iguals a '0', en cas contrari cal mostrar un error tipus 'ValueError'.

L'error el pots mostrar amb la següent instrucció:
raise ValueError("MISSATGE D'ERROR")

Paràmetres:
- list_numbers: Llista de nombres enters positius.

Exemple:
     Entrada:
     sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

     Sortida:
     30

'''

def sum_odd_numbers(list_numbers):
    suma = 0
    for i in list_numbers:
        if not isinstance(i, int):
            raise ValueError("Nombre no enter")
        elif i < 0:
            raise ValueError("Nombre menor que 0")
        if i%2 != 0:
            suma += i
    return suma

# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))
