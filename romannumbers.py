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
# Diccionario de Símbolos Romanos
simbolos = {
    1: "I", 4: "IV", 5: "V",
    9: "IX", 10: "X", 40: "XL",
    50: "L", 90: "XC", 100: "C",
    400: "CD", 500: "D", 900: "CM",
    1000: "M"
}

# Función convertir cualquier numero a romano
def entero_a_romano(n_ent):

    resultado = ""
    n  = n_ent
    numeros = sorted(simbolos.keys(), reverse=True) # Descomponemos el numero de mayor a menor con los valores del diccionario 

    # Encuentra el valor mas alto que tenga el diccionario segun la entrada y le resta el valor del diccionario. Acomula en Resultado los simbolos del diccionario
    for num in numeros:

        while n_ent >= num:

            resultado += simbolos[num]
            n_ent -= num

    return resultado

# Cojemos el numero y lo dividimos en subcadenas de 3, en caso de no ser completa la subcadena la rellena de 0 para que no pete. 
def longitud(numero):

    numero = str(numero)

    while len(numero)%3 != 0:
        numero= "0" + numero

    return numero

# Esta función añade n paréntesis en función de la necesidad de los mismos, además, tiene la lógica incorporada para los numeros menores a 3999 y superiores al mismo.
def devolver_total_romano(numero):

    num = str(numero)
    simbolo_romano = ""
    num_parentesis = 0

    # Elige entre los numeros iferiores a 4 digitos o superiores al mismo
    if len(num) <= 4:

        if numero<=3999: # Coge los numeros inferiores al límite del conteo romano simple

            simbolo_romano = entero_a_romano(numero)

        else: # Captura apartir del 4000 y le añade la lógica del parentesis. Controla el error de las 4M envez del (IV)

            simbolo_romano = "(" + entero_a_romano(int(num[0])) + ")"
            simbolo_romano = simbolo_romano + entero_a_romano(int(num[-3:]))

    else: # Todos los numeros superiores a 4 dígitos entran por aquí

        num = longitud(num)

        while len(num)>4: # Mientras la lonitud del numero sea mayor a 4 se concatena la representación en numeros romanos de los últimos 3 dígitos 
                
                simbolo_romano = "("* num_parentesis + entero_a_romano(int(num[-3:])) + ")" * num_parentesis + simbolo_romano
               
                # Si esta vacía la cadena se restablece.
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





