from ejercicio03 import agrupar_por_inicial

# Correcto
def test_recibe_lista():
    assert agrupar_por_inicial(["trato", "minimo", "hola"]) == {'h': {'hola'}, 'm': {'minimo'}, 't': {'trato'}}

# Correcto
def test_devuelve_diccionario():
    assert agrupar_por_inicial(["mesa", "plato", "mesilla"]) == {'m': {'mesa', 'mesilla'}, 'p': {'plato'}}

# Fallo
def test_ignora_vacios():
    assert agrupar_por_inicial([""]) == None