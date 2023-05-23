simbolos = {
    "I": 1,
}

def Romano_a_entero(letras):
    if letras in simbolos:
        return simbolos[letras]
    