import socket

from .Terminal import Terminal

class TicTackToe:

    grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turn = "X"
    player1 = "X"
    player2 = "O"
    winner = 0
    game_over = False

    turn_counter = 0

    term = Terminal()

    def host_game(self, host, port):
        self.reset_game_data()
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = socket.gethostbyname(socket.gethostname())
        if host == "":
            try:
                server_socket.bind((server_ip, port))

            except socket.gaierror:
                print("[ERROR] Given PORT is not valid!")
                input("[ALERT] Enter any key to continue...")
                return None

            except:
                print("[ERROR] Given IP is not valid!")
                input("[ALERT] Enter any key to continue...")
                return None
        else:
            try:
                server_socket.bind((host, port))
            except:
                print("[ERROR] Given IP is not valid!")
                input("[ALERT] Enter any key to continue...")
                return None


        server_socket.listen(2)

        print("--------------------")
        print(f"| Game hosted on {server_ip} with port: {port} |")
        print("--------------------")
        print("[INFO] Waiting for players...")

        client_socket, address = server_socket.accept()
        print(f"[INFO] Player connected from: {address}")
        self.handle_conn(client_socket)
        client_socket.close()

    def conn_to_game(self, host, port):
        self.reset_game_data()
        print("[INFO] Connecting...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = socket.gethostbyname(socket.gethostname())

        if host == "":
            try:
                client_socket.connect((server_ip, port))

            except:
                print("[ERROR] Given IP is not valid!")
                input("[ALERT] Enter any key to continue...")
                return None

        else:
            try:
                client_socket.connect((host, port))
                
            except:
                print("[ERROR] Given IP is not valid!")
                input("[ALERT] Enter any key to continue...")
                return None

        print("[INFO] Connected!")
        self.player1 = "O"
        self.player2 = "X"
        self.handle_conn(client_socket)
        client_socket.close()

    def handle_conn(self, socket: socket.socket):
        while not self.game_over:
            if self.turn == self.player1:
                self.print_grid()
                try:
                    move = input("[INFO] Enter your move (row, column): ")
                except:
                    print("")
                    print("[INFO] Exiting... Bye bye :)")
                    break
                
                if self.is_move_valid(move.split(",")):
                    self.apply_move(move.split(","), self.player1)
                    self.turn = self.player2
                    socket.send(move.encode())
                else:
                    print("[ERROR] Invalid move!")
                    input("[ALERT] Enter any key to continue...")
            else:
                self.print_grid()
                print("[INFO] Waiting for move...")
                game_data = socket.recv(1024)
                
                if not game_data:
                    break
                else:
                    self.apply_move(game_data.decode().split(","), self.player2)
                    self.turn = self.player1
            
        print("[INFO] Cloasing connection...")
        input("[ALERT] Enter any key to continue...")

    def apply_move(self, move_cords: list, player: str):
        if self.game_over: return
        
        self.turn_counter += 1
        self.grid[int(move_cords[0])][int(move_cords[1])] = player
        self.print_grid()
        if self.is_game_over():
            if self.winner == self.player1:
                print("[ALERT] ------------------")
                print("[ALERT] |   YOU WON!!!   |")
                print("[ALERT] ------------------")
                
            elif self.winner == self.player2:
                print("[ALERT] -------------------")
                print("[ALERT] |   YOU LOSE!!!   |")
                print("[ALERT] -------------------")

        else:
            if self.turn_counter == 9:
                self.game_over = True
                print("[ALERT] -------------------")
                print("[ALERT] |      TIE!!!     |")
                print("[ALERT] -------------------")


    def is_move_valid(self, move_cords: list):
        try:
            return self.grid[int(move_cords[0])][int(move_cords[1])] == " "
            
        except:
            return False

    def is_game_over(self):
        for row in range(3):
            if self.grid[row][0] == self.grid[row][1] == self.grid[row][2] != " ":
                self.winner = self.grid[row][0]
                self.game_over = True
                return True
        
        for column in range(3):
            if self.grid[0][column] == self.grid[1][column] == self.grid[2][column] != " ":
                self.winner = self.grid[0][column]
                self.game_over = True
                return True

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            self.winner = self.grid[0][0]
            self.game_over = True
            return True
        
        if self.grid[2][2] == self.grid[1][1] == self.grid[2][0] != " ":
            print(f"{self.grid[2][2]}:{self.grid[1][1]}:{self.grid[2][0]}")
            self.winner = self.grid[0][0]
            self.game_over = True
            return True

    def print_grid(self):
        self.term.clear_terminal()
        print("#=============#")
        for row in range(3):
            print("#  " + " | ".join(self.grid[row]) + "  #")
            if row != 2:
                print("# ----------- #")

        print("#=============#")

    def reset_game_data(self):
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
        self.player1 = "X"
        self.player2 = "O"
        self.winner = 0
        self.game_over = False
        self.turn_counter = 0
