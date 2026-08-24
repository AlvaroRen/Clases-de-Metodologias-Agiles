from rover import Rover

def test_rover_informa_posicion_y_orientacion_iniciales():
    rover = Rover(x=0, y=0, orientation="N")

    assert rover.position() == (0, 0)
    assert rover.orientation() == "N"

def test_rover_gira_a_la_derecha():
    rover = Rover(x=0, y=0, orientation="N")
    rover.turn_right()

    assert rover.orientation() == "E"
