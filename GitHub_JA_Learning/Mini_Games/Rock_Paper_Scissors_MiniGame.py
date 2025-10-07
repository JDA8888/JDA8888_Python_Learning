import random

def get_choices():
    """
    Ask the player to pick 'rock', 'paper', or 'scissors',
    or allow them to quit the game.
    Randomly select one of the options for the computer.

    Returns:
        dict: A dictionary with the player's choice and computer's choice.
              Example: {"player": "rock", "computer": "scissors"}
              If player chooses 'quit', computer will be None.
    """
    player_choice = input("Please pick rock, paper, or scissors (or type 'quit' to exit): ").lower()
    options = ["rock", "paper", "scissors"]

    if player_choice == "quit":
        return {"player": "quit", "computer": None}

    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}


def check_win(player, computer):
    """
    Determine the winner of a rock-paper-scissors game.

    Args:
        player (str): The player's choice ("rock", "paper", or "scissors")
        computer (str): The computer's randomly chosen option

    Returns:
        str: A message describing the result (win/lose/tie).
    """
    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        return "It's a tie!"

    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."

    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."

    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

    else:
        return "Invalid choice. Please pick rock, paper, or scissors."


# -------------------------------
# Main program loop
# -------------------------------
if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        choices = get_choices()

        # Exit condition
        if choices["player"] == "quit":
            print("Thanks for playing! Goodbye 👋")
            break

        # Get result of the round
        result = check_win(choices["player"], choices["computer"])
        print(result)
        print("-" * 40)  # separator for readability