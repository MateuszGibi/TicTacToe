from lib.TicTacToe import TicTackToe
from lib.Terminal import Terminal

game = TicTackToe()
terminal = Terminal()

while True:
    terminal.clear_terminal()
    terminal.main_menu()
    try:
        option = int(input("Select one option: "))
    except:
        print("[ERROR] Chose correct option!")
        input("[ALERT] Enter any key to continue...")
        continue

    if option == 1:
        game_ip = terminal.get_game_ip()

        try:
            game_port = terminal.get_game_port()
        except:
            print(f"[ERROR] Given PORT is not valid!")
            input("[ALERT] Enter any key to continue...")
            continue

        game.host_game(game_ip, game_port)   
    elif option == 2:
        game_ip = terminal.get_game_ip()

        try:
            game_port = terminal.get_game_port()
        except:
            print(f"[ERROR] Given PORT is not valid!")
            input("[ALERT] Enter any key to continue...")
            continue

        game.conn_to_game(game_ip, game_port)
    
    elif option == 0:
        print("[INFO] Exiting... Bye bye :)")
        break

    else:
        print("[ERROR] Chose correct option!")
        input("[ALERT] Enter any key to continue...")
