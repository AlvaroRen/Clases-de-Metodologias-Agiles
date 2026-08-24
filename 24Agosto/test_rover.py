from rover import Rover

def test_rover_informa_posicion_y_orientacion_iniciales():
    rover = Rover(x=0, y=0, orientation="N")

    assert rover.position() == (0, 0)
    assert rover.orientation() == "N"

