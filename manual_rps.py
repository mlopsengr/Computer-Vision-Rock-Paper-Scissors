import numpy as np
import random

# this python code is created to build the model for the game rock paper scissors

class game:
    def get_computer_choice(self) -> str:
        # this function is used to get the computer choice from rock, paper or scissors
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        return computer_choice

    def get_user_choice(self) -> str:
        # this function is used to get the user's choice of rock, paper or scissors
        user_choice = input("Please enter your choice:")
        return user_choice


    def get_winner(self, computer_choice, user_choice) -> str:
        # this function is used to get the winner of the game
        if computer_choice == user_choice:
            return "It's a tie!"
        elif computer_choice == 'rock':
            if user_choice == 'paper':
                return "You win!"
            else:
                return "You lose!"
        elif computer_choice == 'paper':
            if user_choice == 'scissors':
                return "You win!"
            else:
                return "You lose!"
                    
            
        
        