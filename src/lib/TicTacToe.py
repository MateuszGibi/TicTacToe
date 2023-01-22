import socket
import threading

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
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = socket.gethostbyname(socket.gethostname())
        if host == "":
            server_socket.bind((server_ip, port))
        else:
            server_socket.bind((host, port))

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
        print("[INFO] Connecting...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # client_socket.connect((host, port))
        server_ip = socket.gethostbyname(socket.gethostname())
        if host == "":
            client_socket.connect((server_ip, port))

        else:
            client_socket.connect((host, port))

        print("[INFO] Connected!")
        self.player1 = "O"
        self.player2 = "X"
        self.handle_conn(client_socket)
        #threading.Thread(target=self.handle_conn, args=(client_socket,)).start()
        #client_socket.close()

    def handle_conn(self, socket: socket.socket):
        self.turn = "X"
        while not self.game_over:
            if self.turn == self.player1:
                move = input("[INFO] Enter your move (row, column): ")
                if self.is_move_valid(move.split(",")):
                    self.apply_move(move.split(","), self.player1)
                    self.turn = self.player2
                    socket.send(move.encode())
                else:
                    print("[ERROR] Invalid move!")
            else:
                print("[INFO] Waiting for move...")
                game_data = socket.recv(1024)
                
                if not game_data:
                    break
                else:
                    self.apply_move(game_data.decode().split(","), self.player2)
                    self.turn = self.player1
            
        print("[INFO] Cloasing connection...")
        input("[ALERT] Enter any key to contenue...")

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
                print("[ALERT] -------------------")
                print("[ALERT] |      TIE!!!     |")
                print("[ALERT] -------------------")


    def is_move_valid(self, move_cords: list):
        return self.grid[int(move_cords[0])][int(move_cords[1])] == " "

    def is_game_over(self):
        for row in range(3):
            if self.grid[row][0] == self.grid[row][1] == self.grid[row][2] != " ":
                print(f"{self.grid[row][0]}:{self.grid[row][1]}:{self.grid[row][2]}")
                self.winner = self.grid[row][0]
                self.game_over = True
                return True
        
        for column in range(3):
            if self.grid[0][column] == self.grid[1][column] == self.grid[2][column] != " ":
                print(f"{self.grid[0][column]}:{self.grid[1][column]}:{self.grid[2][column]}")
                self.winner = self.grid[0][column]
                self.game_over = True
                return True

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            print(f"{self.grid[0][0]}:{self.grid[1][1]}:{self.grid[2][2]}")
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
        for row in range(3):
            print("|".join(self.grid[row]))
            if row != 2:
                print("----------")
