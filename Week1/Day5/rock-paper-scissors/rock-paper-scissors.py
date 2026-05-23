from game import Game


def get_user_menu_choice():
    print("\tMenu:")
    print("\t(g) Play a new game")
    print("\t(x) Show scores and exit")
    try:
        choice = input("\t : ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return "x"
    if choice in ("g", "x"):
        return choice
    return None


def print_results(results):
    try:
        print("\t Game Results:")
        print(f"\t  You won {results['win']} times")
        print(f"\t  You lost {results['loss']} times")
        print(f"\t  You drew {results['draw']} times")
        print("\n\t Thank you for playing!")
    except KeyError as e:
        print(f"\tMissing result key: {e}")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "g":
            try:
                game = Game()
                result = game.play()
                results[result] = results.get(result, 0) + 1
            except Exception as e:
                print(f"\tAn error occurred during the game: {e}")
        elif choice == "x":
            print_results(results)
            break
        else:
            print("\tInvalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\tGame interrupted. Goodbye!")
    except Exception as e:
        print(f"\n\tFatal error: {e}")
