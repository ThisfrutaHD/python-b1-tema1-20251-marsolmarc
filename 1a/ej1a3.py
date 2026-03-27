'''
Enunciat:
Implementa una funció anomenada "invert_text(text_chain)" que rebi com
paràmetre una cadena de text de tipus string anomenada 'text_chain' i torni
el text invertit.

Paràmetres:
- text_chain: Aquest paràmetre només admet strings.

Exemple:
     Entrada:
     invert_text('Hello world!')

     Sortida:
     !dlrow olleH

'''

def invert_text(text_chain:str):
    return text_chain[::-1]
 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(invert_text("Hello world!"))