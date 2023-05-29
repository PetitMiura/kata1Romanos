from romannumbers import *

class RomanNumber:
    def __init__(self, entrada):
        # if isinstance(entrada, int): # funcion d python q comprueva el primer parametro si es str o int
        if type(entrada) == int:
            self._numero = entrada
            self._simbolo = entero_a_romano(entrada)
        elif type(entrada) == str:
            self._numero = romano_a_entero(entrada)
            self._simbolo = entrada
        else:
            raise RomanNumberError("No se admiten decimales")
        
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, entrada):
        self._numero = entrada
        self._simbolo = entero_a_romano(entrada)
    
    @property
    def simbolo(self):
        return self._simbolo
    
    @simbolo.setter
    def simbolo(self, entrada):
        self._simbolo = entrada
        self._numero = romano_a_entero(entrada)



    '''
    metodos magicos para logica
    ''' 
    def __eq__(self, other):
        return self.numero == other.numero
    
    '''
    metodos mágicos para aritmética
    '''

    def __mul__(self, otro):
        if not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)
        resultado = self.numero * otro.numero
        return RomanNumber(resultado)
    
    def __rmul__(self, otro):
        return self.__mul__(otro)
    '''
    metodos magicos para representación
    '''   
    def __repr__(self):
        return f"{self.numero} - {self.simbolo}"
    def __str__(self):
        return self.__repr__()

