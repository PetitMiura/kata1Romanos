'''
simbolos = {
    1: "I",
    5: "V",
    10: "X"
}

def entero_a_romano(n_int):
    if n_int in simbolos:
        return simbolos[n_int]

    if n_int < 4:
        return n_int * simbolos[1]
    elif n_int == 4:
        return simbolos[1] + simbolos[5]
    elif n_int >5 and n_int < 9:
        multiplicador = n_int - 5
        return simbolos[5] + multiplicador * simbolos[1]
    else:
        return simbolos[1] + simbolos[10]
''' 
simbolos = {
    1: "I", 4: "IV", 5: "V",
    9: "IX", 10: "X", 40: "XL",
    50: "L", 90: "XC", 100: "C",
    400: "CD", 500: "D", 900: "CM",
    1000: "M"
}

def entero_a_romano(n_ent):
    resultado = ""
    n  = n_ent
    numeros = sorted(simbolos.keys(), reverse=True) #1541005040

    for num in numeros:
        while n_ent >= num:
            resultado += simbolos[num]
            n_ent -= num

    return resultado

def longitud(numero):
    numero = str(numero)
    while len(numero)%3 != 0:
        numero= "0" + numero
    return numero

def devolver_total_romano(numero):
    num = str(numero)
    simbolo_romano = ""
    num_parentesis = 0
    if len(num) == 4:
        if numero<=3999:
            simbolo_romano = entero_a_romano(numero)
        else:
            simbolo_romano = "(" + entero_a_romano(int(num[0])) + ")"
            simbolo_romano = simbolo_romano + entero_a_romano(int(num[-3:]))
    else:
        num = longitud(num)
        while len(num)>4:
                simbolo_romano = "("* num_parentesis + entero_a_romano(int(num[-3:])) + ")" * num_parentesis + simbolo_romano
                if simbolo_romano == "()":
                    simbolo_romano = ""
                num = num[:-3]
                num_parentesis += 1
        simbolo_romano = "("* num_parentesis + entero_a_romano(int(num)) + ")"* num_parentesis + simbolo_romano
    return simbolo_romano



print(devolver_total_romano(1))
print(devolver_total_romano(10))
print(devolver_total_romano(100))
print(devolver_total_romano(1000))
print(devolver_total_romano(3999))
print(devolver_total_romano(10000))
print(devolver_total_romano(100000))
print(devolver_total_romano(1000000))
print(devolver_total_romano(10000000))





