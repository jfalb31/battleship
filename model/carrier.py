from . abstract_ship import AbstractShip
from . position import Position


class Carrier(AbstractShip):

    def __init__(self, num_holes, pos, is_vertical, x_size, y_size):
        super().__init__(num_holes, pos, is_vertical, x_size, y_size)

    def get_coords(self):
        coords = []
        if self.is_vertical == 1:
            coords.append(self.pos)
            coords.append(Position(self.pos.x, self.pos.y + 1))
            coords.append(Position(self.pos.x, self.pos.y + 2))
            coords.append(Position(self.pos.x, self.pos.y + 3))
            coords.append(Position(self.pos.x, self.pos.y + 4))
        else:
            coords.append(self.pos)
            coords.append(Position(self.pos.x + 1, self.pos.y))
            coords.append(Position(self.pos.x + 2, self.pos.y))
            coords.append(Position(self.pos.x + 3, self.pos.y))
            coords.append(Position(self.pos.x + 4, self.pos.y))
        return coords
