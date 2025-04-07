import os
import time 
import sys
from menu import display_title, display_production, get_input
from game import display_gameintro, display_loadgame # , display_gameover, display_gameplay, display_gameplay2, display_gameplay3

def clear_screen ():
    # Essa função server para limpar a tela.
    os.system('cls' if os.name == 'nt' else 'clear')

def dottime ():
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')

def display_viola ():
    clear_screen()
    display_production()
    time.sleep(5)

def start_new_game():
    clear_screen()
    display_title()
    time.sleep(5)
    display_gameintro()

def load_saved_game():
    clear_screen()
    display_title()
    time.sleep(5)
    display_loadgame

def menu_principal():
    while True:
        clear_screen()
        display_title()
        print("\n=== Menu Principal ===\n")
        print("1) Novo Jogo")
        print("2) Carregar Jogo")
        print("3) Sair")
        
        choice = get_input(["1", "2", "3"])
        
        if choice == "1":
            start_new_game()
        elif choice == "2":
            load_saved_game()
        elif choice == "3":
            print("\nObrigado por jogar Explorador de Masmorras!")
            sys.exit(0)

def display_intro():
    # Essa função serve para mostrar a tela de introdução.
    clear_screen()
    display_title()
    print("=============================================================================================================")
    print("                                            Terror no Mount San Gorgono                                      ")
    print("=============================================================================================================")    
    print("\n")
    print("\n")
    menu_principal()



  
# display_viola()
display_intro()