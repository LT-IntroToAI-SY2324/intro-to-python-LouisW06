# We will write a rock paper scissors game in class - Complete it in this file
import random



def get_choices():
    options = ['rock', 'paper', 'scissors']
    choice = input("Enter a choice (rock, paper, or scissors)")
    AI_choice = random.choice(options)
    choices = {"player": choice, "computer": AI_choice}

    return choices
#I am a pro coder now (:

def checkwinner(player, computer):
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "You tied"
    elif player == "rock":
        if computer == "scissors":
            return "Rock crushes scissors. You win"
        else:
            return "Paper engulfs rock. You lose"
    elif player == "paper":
        if computer == "rock":
            return "Paper engulfs rock. You win"
        else:
            return "Scissors slice paper. You lose"
    elif player == "scissors":
        if computer == "rock":
            return "Rock crushes scissors. You lose"
        else:
            return "Scissors slice paper. You win"
        


choices = get_choices()
#print(choices)
result = checkwinner(choices["player"], choices["computer"])
print(result)
#result = checkwinner("scissors", "paper")
#print(result)