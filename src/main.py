from lib.TicTacToe import TicTackToe
from lib.Terminal import Terminal

game = TicTackToe()
terminal = Terminal()

while True:
    terminal.main_menu()
    option = int(input("Select one option: "))
    if option == 1:
        game_ip = terminal.get_game_ip()
        game_port = terminal.get_game_port()
        game.host_game(game_ip, game_port)   
    elif option == 2:
        game_ip = terminal.get_game_ip()
        game_port = terminal.get_game_port()
        game.conn_to_game(game_ip, game_port)
    
    else:
        print("[INFO] Exiting... Bye bye :)")
        break
