import pytest
from ejercicio01 import normaliza_nombre

# Fallo
def test_str():
    assert normaliza_nombre("jose angel  FErnandez") == "Jose Angel Fernandez"

# Correcto
def test_formato():
    assert normaliza_nombre("jose antonio") == "Jose Antonio"

# Correcto
def test_guiones():
    assert normaliza_nombre("Ana-maria Morales") == "Ana-maria Morales"

# Fallo
def test_tipo():
    assert normaliza_nombre(3) == TypeError()