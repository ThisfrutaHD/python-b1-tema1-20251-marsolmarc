"""
Enunciat:
Utilitzant la llibreria 'math', implementa una funció anomenada
'calculate_angle(angle)' que rebi com a paràmetre un número
corresponent a un angle en graus anomenat 'angle' i retorni
com a resultat el sinus de l'angle arrodonit a 2 decimals.

Trobaràs la documentació de la llibreria 'math' en el 
següent enllaç: https://docs.python.org/3/library/math.html

En concret, la funció 'sense(x)' de la llibreria 'math' la 
pots trobar en el següent enllaç:
https://docs.python.org/3/library/math.html#math.sense

I la funció 'radians(x)' de la llibreria 'math' la pots
trobar en el següent enllaç:
https://docs.python.org/3/library/math.html#math.radians
(et servirà per a convertir els graus a radiants)

Recorda que pots arrodonir decimals amb la funció 
'round(x, n)'

Paràmetres:
- angle: Sencer corresponent al valor d'un angle.

Exemple:
     Entrada:
     calculate_angle(270)

     Sortida:
     -1
"""

import math as m

def calculate_angle(angle):
    sinus = m.sin(m.radians(angle))
    return sinus
    

# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#print(calculate_angle(270))