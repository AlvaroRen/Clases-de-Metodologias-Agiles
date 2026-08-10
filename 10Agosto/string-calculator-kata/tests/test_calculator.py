from src.calculator import sumar

def test_string_vacio_devuelve_cero():
    assert sumar("") == 0

def test_un_numero_devuelve_ese_numero():
    assert sumar("1") == 1

def test_dos_numeros_separados_por_coma_se_suman():
    assert sumar("1,2") == 3

def test_numeros_separados_por_salto_de_linea_se_suman():
    assert sumar("1\n2,3") == 6