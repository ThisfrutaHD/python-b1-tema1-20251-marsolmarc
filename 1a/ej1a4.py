'''
Enunciat:
Crea una funció anomenada "count_vowels(text_chain)" que rebi com a paràmetre
una cadena de text de tipus string anomenada 'text_chain' i retorni el número
de vocals, ja siguin majúscules o minúscules, sense accent, que es trobin en 
aquesta cadena de text.

Paràmetres:
- text_chain: Aquest paràmetre només admet strings.

Exemple:
     Entrada:
     count_vowels('Hello world, this is an example.')

     Sortida:
     9

'''

def count_vowels(text_chain:str):
    vowels = "aAeEiIoOuU"
    count = 0
    for i in text_chain:
        if i in vowels:
            count += 1
    return count

# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(count_vowels("Hello world, this is an example."))