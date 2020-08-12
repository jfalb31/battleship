from . abstract_ship import AbstractShip
from . position import Position


class PatrolBoat(AbstractShip):

    def __init__(self, num_holes, pos, is_vertical, x_size, y_size):
        super().__init__(num_holes, pos, is_vertical, x_size, y_size)

    def get_coords(self):
        coords = []
        if self.is_vertical == 1:
            coords.append(self.pos)
            coords.append(Position(self.pos.x, self.pos.y + 1))
        else:
            coords.append(self.pos)
            coords.append(Position(self.pos.x + 1, self.pos.y))
        return coords
