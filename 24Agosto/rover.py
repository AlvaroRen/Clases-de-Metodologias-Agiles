
class Rover:

    ORIENTATIONS = ["N", "E", "S", "O"]

    _DELTAS = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "O": (-1, 0),
    }

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

    def move_forward(self):
        self._y += 1

    def move_forward(self):
        dx, dy = self._DELTAS[self.orientation()]
        self._x += dx
        self._y += dy