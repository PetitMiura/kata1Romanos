simbolos = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10
}

def romano_a_entero(digito):
    res = 0
    i = 0
    while i < len(digito): # Recorremos el dígito romano secuencialmente
        if digito[i:i+2] in simbolos: # Se verifica si la subcadena de longitud 2 a partir de la posición i del dígito romano está presente en el diccionario simbolos. Esto nos permite detectar las combinaciones especiales como "IV" y "IX
            res += simbolos[digito[i:i+2]]
            i += 2
        else:
            res += simbolos[digito[i]]
            i += 1
    return res