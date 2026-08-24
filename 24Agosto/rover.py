
class Rover:

    ORIENTATIONS = ["N", "E", "S", "O"]

    def __init__(self, x, y, orientation):
        self._x = x
        self._y = y
        self._orientation_index = self.ORIENTATIONS.index(orientation)

    def position(self):
        return (self._x, self._y)

    def orientation(self):
        return self.ORIENTATIONS[self._orientation_index]

    def turn_right(self):
        self._orientation_index = (self._orientation_index + 1) % 4

    def turn_left(self):
        self._orientation_index = (self._orientation_index - 1) % 4