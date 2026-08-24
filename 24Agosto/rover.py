
class Rover:
    def __init__(self, x, y, orientation):
        self._x = x
        self._y = y
        self._orientation = orientation

    def position(self):
        return (self._x, self._y)

    def orientation(self):
        return self._orientation

    def turn_right(self):
        self._orientation = "E"

    def turn_left(self):
        self._orientation = "O"