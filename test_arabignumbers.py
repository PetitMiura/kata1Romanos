from arabignumbers import romano_a_entero
import pytest


def test_I_es_uno():
    assert romano_a_entero("I") == 1
def test_II_es_uno():
    assert romano_a_entero("II") == 2

def test_III_es_uno():
    assert romano_a_entero("III") == 3
def test_IV_es_uno():
    assert romano_a_entero("IV") == 4
def test_V_es_uno():
    assert romano_a_entero("V") == 5
def test_VI_es_uno():
    assert romano_a_entero("VI") == 6
def test_VII_es_uno():
    assert romano_a_entero("VII") == 7
def test_VIII_es_uno(): 
    assert romano_a_entero("VIII") == 8
def test_IX_es_uno():
    assert romano_a_entero("IX") == 9
def test_X_es_uno():
    assert romano_a_entero("X") == 10
'''
def test_MMMCMXCIX_es_uno():
    assert romano_a_entero("MMMCMXCIX") == 3999
'''