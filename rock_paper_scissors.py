# We will write a rock paper scissors game in class - Complete it in this file
import random



choice = "rock"
AI_choice = "paper"
def get_choices():
    options = ['rock', 'paper', 'scissors']
    choice = "rock"
    AI_choice = random.choice(options)
    choices = {"player": choice, "computer": AI_choice}

    return choices
#I am a pro coder now (:
choices = get_choices()
print(choices)