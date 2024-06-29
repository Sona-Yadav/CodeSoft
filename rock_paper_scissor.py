import random
from termcolor import colored


class Game:
    # Foreground colors for rock, paper, and scissors
    Rock = colored("Rock", "magenta", attrs=["blink"])
    Paper = colored("Paper", "dark_grey", attrs=["blink"])
    Scissors = colored("Scissors", "light_blue", attrs=["blink"])

    def __init__(self):
        self.options = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            user_choice = input(
                f"\nChoose {Game.Rock}[r], {Game.Paper}[p], or {Game.Scissors}[s]: "
            ).lower()
            if user_choice in self.options or user_choice in ["r", "p", "s"]:
                if len(user_choice) == 1:
                    user_choice = {
                        "r": "rock",
                        "p": "paper",
                        "s": "scissors",
                    }[user_choice]
                break
            else:
                print(
                    f"Invalid choice. Please choose {Game.Rock}, {Game.Paper}, or {Game.Scissors}."
                )

        return user_choice

    def get_computer_choice(self):
        return random.choice(self.options)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return colored(
                f"Both players selected {user_choice}, It's a tie!",
                "yellow",
                attrs=["blink"],
            )
        elif user_choice in ["rock", "r"]:
            if computer_choice == "scissors":
                return colored(
                    f"{Game.Rock} smashes {Game.Scissors}! You win!",
                    "green",
                    attrs=["blink"],
                )
            else:
                return colored(
                    f"{Game.Paper} covers {Game.Rock}! You lose.",
                    "red",
                    attrs=["blink"],
                )
        elif user_choice in ["paper", "p"]:
            if computer_choice == "rock":
                return colored(
                    f"{Game.Paper} covers {Game.Rock}! You win!",
                    "green",
                    attrs=["blink"],
                )
            else:
                return colored(
                    f"{Game.Scissors} cuts {Game.Paper}! You lose.",
                    "red",
                    attrs=["blink"],
                )
        elif user_choice in ["scissors", "s"]:
            if computer_choice == "paper":
                return colored(
                    f"{Game.Scissors} cuts {Game.Paper}! You win!",
                    "green",
                    attrs=["blink"],
                )
            else:
                return colored(
                    f"{Game.Rock} smashes {Game.Scissors}! You lose.",
                    "red",
                    attrs=["blink"],
                )

    def play_game(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()

            print(
                f"YOU CHOOSE [ {user_choice}] . COMPUTER CHOOSE [ {computer_choice} ]."
            )

            result = self.determine_winner(user_choice, computer_choice)
            print(result)

            if "win" in result:
                self.user_score += 1
            elif "lose" in result:
                self.computer_score += 1

            print(f"Score - You: {self.user_score}, Computer: {self.computer_score}")

            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again != "y":
                print("\n----------------\n")
                print(
                    "Final score: "
                    + f"You: {self.user_score}, Computer: {self.computer_score}"
                )
                if self.user_score > self.computer_score:
                    print(
                        colored(
                            f"You win! Congratulations!",
                            "green",
                            attrs=["blink"],
                        )
                    )

                elif self.user_score == self.computer_score:
                    print(
                        colored(
                            f"It's a tie!",
                            "yellow",
                            attrs=["blink"],
                        )
                    )
                else:
                    print(
                        colored(
                            f"You lose! Better luck next time!",
                            "red",
                            attrs=["blink"],
                        )
                    )

                print("\n----------------\n")

                break


if __name__ == "__main__":
    rps_game = Game()
    rps_game.play_game()
