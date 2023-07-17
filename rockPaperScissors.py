import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, or scissors): ")
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, and the computer chose {computer}.") #f string
    if player == computer:
        return "It's a Tie."
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You Won!"
        else:
            return "Paper covers rock! You Lose."
    elif player == "paper":
        if computer == "scissors":
            return "Scissors chops paper! You Lose."
        else:
            return "Paper covers rock! You Win!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors chops paper! You Won!"
        else:
            return "Rock smashes scissors! You Lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
