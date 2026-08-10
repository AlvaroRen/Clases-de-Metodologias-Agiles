from src.calculator import sumar

def test_string_vacio_devuelve_cero():
    assert sumar("") == 0