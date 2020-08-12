from abc import abstractmethod


class AbstractShip:

    def __init__(self, num_holes, pos, is_vertical, x_size, y_size):
        # re-position if the ship is off the board
        if is_vertical == 1 and pos.y + (num_holes - 1) > y_size:
            pos.y = y_size - num_holes
        elif pos.x + (num_holes - 1) > x_size:
            pos.x = x_size - num_holes

        self.num_holes = num_holes
        self.pos = pos
        self.is_vertical = is_vertical

        super().__init__()

    def print_coords(self):
        for coord in self.get_coords():
            print(str(coord.x) + "," + str(coord.y))

    def is_hit(self, x, y):
        carrier_coords = self.get_coords()
        for coord in carrier_coords:
            if coord.x == x and coord.y == y:
                return True
        return False

    @abstractmethod
    def get_coords(self):
        pass
