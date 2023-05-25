from romannumbers import *

def test_instanciar_un_numero_romano():
    romano = RomanNumber(23)
    assert romano.valor == 23
    assert romano.simbolo == "XXIII"