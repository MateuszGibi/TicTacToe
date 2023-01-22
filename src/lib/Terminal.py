import os 
import socket

class Terminal:

    def logo(self):
        print("                              ___                       ___           ___                       ___           ___     ")
        print("      ___       ___          /  /\          ___        /  /\         /  /\          ___        /  /\         /  /\    ")
        print("     /  /\     /  /\        /  /:/         /  /\      /  /::\       /  /:/         /  /\      /  /::\       /  /:/_   ")
        print("    /  /:/    /  /:/       /  /:/         /  /:/     /  /:/\:\     /  /:/         /  /:/     /  /:/\:\     /  /:/ /\  ")
        print("   /  /:/    /__/::\      /  /:/  ___    /  /:/     /  /:/~/::\   /  /:/  ___    /  /:/     /  /:/  \:\   /  /:/ /:/_ ")
        print("  /  /::\    \__\/\:\__  /__/:/  /  /\  /  /::\    /__/:/ /:/\:\ /__/:/  /  /\  /  /::\    /__/:/ \__\:\ /__/:/ /:/ /\\")
        print(" /__/:/\:\      \  \:\/\ \  \:\ /  /:/ /__/:/\:\   \  \:\/:/__\/ \  \:\ /  /:/ /__/:/\:\   \  \:\ /  /:/ \  \:\/:/ /:/")
        print(" \__\/  \:\      \__\::/  \  \:\  /:/  \__\/  \:\   \  \::/       \  \:\  /:/  \__\/  \:\   \  \:\  /:/   \  \::/ /:/ ")
        print("      \  \:\     /__/:/    \  \:\/:/        \  \:\   \  \:\        \  \:\/:/        \  \:\   \  \:\/:/     \  \:\/:/  ")
        print("       \__\/     \__\/      \  \::/          \__\/    \  \:\        \  \::/          \__\/    \  \::/       \  \::/   ")
        print("                             \__\/                     \__\/         \__\/                     \__\/         \__\/    ")
    
    def main_menu(self):
        self.logo()
        print("1. Host game")
        print("2. Connect to the game")
        print("0. Exit")
    
    def get_game_port(self):
        return int(input("Insert game port: "))
                        
    def get_game_ip(self):
        return input(f"Insert game host's ip ({socket.gethostbyname(socket.gethostname())}): ")

    def clear_terminal(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


