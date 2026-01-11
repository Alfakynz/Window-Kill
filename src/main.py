import signal
import sys
from game import Game
from test import jeux_de_test

def main() -> None:
    Game()

# Made by ChatGPT to handle Ctrl+C gracefully (try & except doesn't work well with Pyxel)
def handle_interrupt(sig, frame) -> None:
    print("\nGame interrupted by user. Exiting gracefully...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_interrupt)
    main()
    """print("1. Lancer le jeu")
    print("2. Tester les jeux de test")
    print("3. Faire les jeux de test puis lancer le jeu")
    choice = input("Que voulez vous faire ? (Choisissez le numéro) ")

    match choice:
        case "1":
            signal.signal(signal.SIGINT, handle_interrupt)
            main()
        case "2":
            signal.signal(signal.SIGINT, handle_interrupt)
            jeux_de_test()
        case "3":
            signal.signal(signal.SIGINT, handle_interrupt)
            jeux_de_test()
            signal.signal(signal.SIGINT, handle_interrupt)
            main()
        case _:
            print("Le choix n'existe pas")"""