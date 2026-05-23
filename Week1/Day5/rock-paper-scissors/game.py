import random


class Game:
    items = ("rock", "paper", "scissors")

    def get_user_item(self):
        mapping = {"r": "rock", "p": "paper", "s": "scissors"}
        while True:
            try:
                choice = input("Select (r)ock, (p)aper, or (s)cissors: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nInput cancelled. Defaulting to rock.")
                return "rock"
            if choice in mapping:
                return mapping[choice]
            if choice in self.items:
                return choice
            print("Invalid choice. Please try again.")

    def get_computer_item(self):
        try:
            return random.choice(self.items)
        except IndexError:
            return "rock"

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        wins = {
            ("rock", "scissors"),
            ("scissors", "paper"),
            ("paper", "rock"),
        }
        if (user_item, computer_item) in wins:
            return "win"
        return "loss"

    def play(self):
        try:
            user_item = self.get_user_item()
            computer_item = self.get_computer_item()
            result = self.get_game_result(user_item, computer_item)
            user_short = user_item[0]
            computer_short = computer_item[0]
            print(f"You chose: {user_short}. The computer chose: {computer_short}. Result: {result}")
            return result
        except Exception as e:
            print(f"An unexpected error occurred while playing: {e}")
            return "draw"
