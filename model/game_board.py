from . carrier import Carrier
from . battleship import Battleship
from . submarine import Submarine
from . patrol_boat import PatrolBoat
from . position import Position

import random


class GameBoard:

    y_size = 9
    x_size = 9

    def __init__(self):

        self.carrier = self.create_carrier()

        self.battleship = self.create_battleship(self.carrier)

        self.submarine = self.create_submarine(self.carrier, self.battleship)

        self.patrol_boat = self.create_patrol_boat(
                            self.carrier,
                            self.battleship,
                            self.submarine)

        self.own_board = [
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                        ]
        self.guess_board = [
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                            [
                                False, False, False,
                                False, False, False,
                                False, False, False
                            ],
                        ]

        super().__init__()

    def ships_pos(self):
        return "Carrier pos: (" + str(self.carrier.pos.x) + "," + \
                                str(self.carrier.pos.x) + ")\n" + \
                                "Battleship pos: (" + str(self.battleship.pos.x) + \
                                "," + str(self.battleship.pos.y) + ")\n" + \
                                "Submarine pos: (" + str(self.submarine.pos.x) + \
                                "," + str(self.submarine.pos.y) + ")\n" + \
                                "Patrol Boat: (" + str(self.patrol_boat.pos.x) + \
                                "," + str(self.patrol_boat.pos.y) + ")\n"

    def game_board_display(self):
        output = "   1 2 3 4 5 6 7 8 9\n"
        alpha = [" A", " B", " C", " D", " E", " F", " G", " H", " I"]
        y = 0
        while y < GameBoard.y_size:
            output += alpha[y]
            y += 1
            x = 0
            while x < GameBoard.x_size:
                x += 1
                if self.carrier.is_hit(x, y):
                    output += " c"
                elif self.battleship.is_hit(x, y):
                    output += " b"
                elif self.submarine.is_hit(x, y):
                    output += " s"
                elif self.patrol_boat.is_hit(x, y):
                    output += " p"
                else:
                    output += " x"

            output += "\n"
        return output

    def create_carrier(self):
        return Carrier(
                    5,
                    Position(
                            random.randint(1, GameBoard.x_size),
                            random.randint(1, GameBoard.y_size)
                    ),
                    random.randint(0, 1),
                    GameBoard.x_size,
                    GameBoard.y_size
                )

    def create_battleship(self, carrier):
        has_collissions = True
        while has_collissions:
            temp_battleship = Battleship(
                                4,
                                Position(
                                        random.randint(1, GameBoard.x_size),
                                        random.randint(1, GameBoard.y_size)
                                        ),
                                random.randint(0, 1),
                                GameBoard.x_size,
                                GameBoard.y_size
                            )
            has_carrier_collissions = False
            for coord in carrier.get_coords():
                if temp_battleship.is_hit(coord.x, coord.y):
                    has_carrier_collissions = True
                    break
            if has_carrier_collissions is False:
                has_collissions = False

        return temp_battleship

    def create_submarine(self, carrier, battleship):
        has_collissions = True
        while has_collissions:
            temp_submarine = Submarine(
                                3,
                                Position(
                                        random.randint(1, GameBoard.x_size),
                                        random.randint(1, GameBoard.y_size)
                                        ),
                                random.randint(0, 1),
                                GameBoard.x_size,
                                GameBoard.y_size
                            )
            has_carrier_collissions = False
            for coord in carrier.get_coords():
                if temp_submarine.is_hit(coord.x, coord.y):
                    has_carrier_collissions = True
                    break

            has_battleship_collissions = False
            for coord in battleship.get_coords():
                if temp_submarine.is_hit(coord.x, coord.y):
                    has_battleship_collissions = True
                    break

            if has_carrier_collissions is False and \
                    has_battleship_collissions is False:
                has_collissions = False

        return temp_submarine

    def create_patrol_boat(self, carrier, battleship, submarine):
        has_collissions = True
        while has_collissions:
            temp_patrol_boat = PatrolBoat(
                                2,
                                Position(
                                        random.randint(1, GameBoard.x_size),
                                        random.randint(1, GameBoard.y_size)
                                        ),
                                random.randint(0, 1),
                                GameBoard.x_size,
                                GameBoard.y_size
                            )
            has_carrier_collissions = False
            for coord in carrier.get_coords():
                if temp_patrol_boat.is_hit(coord.x, coord.y):
                    has_carrier_collissions = True
                    break

            has_battleship_collissions = False
            for coord in battleship.get_coords():
                if temp_patrol_boat.is_hit(coord.x, coord.y):
                    has_battleship_collissions = True
                    break

            has_submarine_collissions = False
            for coord in submarine.get_coords():
                if temp_patrol_boat.is_hit(coord.x, coord.y):
                    has_submarine_collissions = True
                    break

            if has_carrier_collissions is False and \
                    has_battleship_collissions is False and \
                    has_submarine_collissions is False:
                has_collissions = False
        return temp_patrol_boat
