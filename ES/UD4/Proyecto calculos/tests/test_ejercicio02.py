import pytest
from ejercicio02 import validar_nif

# Correcto
def test_recibe_NIF():
    assert validar_nif("12345678Z") == True

# Fallo
def test_acepta_minusculas():
    assert validar_nif("12345678z") == True

# Correcto
def test_ignora_espacios():
    assert validar_nif(" 12345678Z") == True

# Correcto
def test_validacion():
    assert validar_nif("12345678W") == False

# Correcto
def test_formato_correcto():
    assert validar_nif("A12342345") == False