'''
Enunciat:
Implementa la funció 'fibonacci(fibonacci_number)' que contingui l'algorisme
de Fibonacci i rebi com a paràmetre un valor numèric enter anomenat
'fibonacci_number' i torneu el valor de la sèrie Fibonacci en aquesta posició.
Així mateix, si el valor no és numèric, o és menor a zero, cal llançar
una excepció ValueError("missatge"), la qual pot incloure un missatge que hi hauria de
correspondre amb el tipus d'error durant la validació.

Paràmetres:
- fibonacci_number: Nombre enter positiu superior a 0 que representa la
posició a la sèrie Fibonacci.

Exemple:
     Entrada:
     fibonacci(10)

     Sortida:
     55

'''

#def fibonacci_recursiu(fibonacci_number: int) -> int: #type hint
#   
#    if not isinstance(fibonacci_number, int):
#        raise ValueError("El nombre ha de ser de tipus int")
#    elif fibonacci_number < 0: #Valor numeric i superior a 0
#        raise ValueError("El nombre ha de ser superior a 0")
#    else:
#        if fibonacci_number == 0: #cas base
#            return 0
#        elif fibonacci_number == 1: #cas base
#            return 1
#        else:
#            return fibonacci_recursiu(fibonacci_number-1) + fibonacci_recursiu(fibonacci_number-2)
        
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#print(fibonacci_recursiu(6))

def fibonacci(fibonacci_number: int):

    if not isinstance(fibonacci_number, int):
        raise ValueError("El nombre ha de ser de tipus int")
    elif fibonacci_number < 0: #Valor numeric i superior a 0
        raise ValueError("El nombre ha de ser superior a 0")
    else:
        b, a = 0, 1
        for i in range(fibonacci_number):
            b, a = a, a+b
        return b

#print(fibonacci(10))