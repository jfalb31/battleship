from model.game_board import GameBoard


is_debug = True
game_running = True
game_in_progress = True

player_gameboard = GameBoard()
cpu_gameboard = GameBoard()


def debug(message):
    if is_debug:
        print(message + "\n")


print("\nBattleship\n")

while game_running:
    main_menu_option = input("1. Start new game\n2. Exit\n\nOption: ")

    if main_menu_option == "2":
        break
    elif main_menu_option == "1":
        print("\nStarting new game...\n")
        player_gameboard = GameBoard()
        debug(player_gameboard.ships_pos())
        debug(player_gameboard.game_board_display())
        player_gameboard.carrier.print_coords()
        cpu_gameboard = GameBoard()
        debug(cpu_gameboard.ships_pos())
        debug(cpu_gameboard.game_board_display())
        while game_in_progress:
            # letter = input("Letter: ")
            # number = input("Number: ")
            break
    else:
        print("\nUnknown option...Please enter a valid option\n")


debug("\nGoodbye!\n")
