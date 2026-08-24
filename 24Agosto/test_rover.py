from rover import Rover

def test_rover_informa_posicion_y_orientacion_iniciales():
    rover = Rover(x=0, y=0, orientation="N")

    assert rover.position() == (0, 0)
    assert rover.orientation() == "N"

def test_rover_gira_a_la_derecha():
    rover = Rover(x=0, y=0, orientation="N")
    rover.turn_right()

    assert rover.orientation() == "E"

def test_rover_gira_a_la_izquierda():
    rover = Rover(x=0, y=0, orientation="N")
    rover.turn_left()

    assert rover.orientation() == "O"

def test_rover_avanza_una_celda_mirando_al_este():
    rover = Rover(x=0, y=0, orientation="E")

    rover.move_forward()

    assert rover.position() == (1, 0)

def test_rover_retrocede_una_celda_sin_cambiar_orientacion():
    rover = Rover(x=0, y=0, orientation="N")

    rover.move_backward()

    assert rover.position() == (0, -1)
    assert rover.orientation() == "N"