import numpy as np
import random

# this python code is created to build the model for the game rock paper scissors

# for milestone 4 : you can creae user score, computer score, number of rounds/run, list of choice (rock, paper, scissors, nothing) in your init method
# also create a get_prediction function and paste the keras model code, little tweaks are needed
# you can use add max under np  to mapp the values 1,2,3,4 to rock, paper, scissors, nothing
# you need to put a countdown timer to the game, so the game ends after a number of runs or time period.

class computer_vision:

    def __init__(self, computer_choice, user_choice) -> None:
        
        self.computer_choice = computer_choice
        self.user_choice = user_choice

        pass

    def get_computer_choice(self) -> str:
        """
        this function is used to get the computer choice from rock, paper or scissors
        """
        
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])
        return self.computer_choice

        pass

    def get_user_choice(self) -> str:
        """
        this function is used to get the user's choice of rock, paper or scissors
        """
        self.user_choice = input("Please enter your choice (rock, paper or scissors):")

        return self.user_choice

        pass


    def get_winner(self) -> str:
        """
        this function is used to get the winner of the game
        """
        if self.computer_choice == self.user_choice:
            return "It's a tie!"
        elif self.computer_choice == 'rock':
            if self.user_choice == 'paper':
                return "You win!"
            else:
                return "You lose!"
        elif self.computer_choice == 'paper':
            if self.user_choice == 'scissors':
                return "You win!"
            else:
                return "You lose!"
        elif self.computer_choice == 'scissors':
            if self.user_choice == "rock":
                return "You win!"
            else:
               return "You lose!"
        # no condition true
        else: 
            return "You have entered an invalid input"

        pass

def play(self):
    
        
            
    
        

      
            
        
        