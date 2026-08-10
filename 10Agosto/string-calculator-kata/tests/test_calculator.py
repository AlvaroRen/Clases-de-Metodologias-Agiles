from src.calculator import sumar

def test_string_vacio_devuelve_cero():
    assert sumar("") == 0

def test_un_numero_devuelve_ese_numero():
    assert sumar("1") == 1