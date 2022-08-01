import numpy as np
import time
import random
import cv2
from keras.models import load_model

# this python code is created to build the model for the game rock paper scissors

# for milestone 4 : you can creae user score, computer score, number of rounds/run, list of choice (rock, paper, scissors, nothing) in your init method
# also create a get_prediction method and paste the keras model code, little tweaks are needed
# you can use add max under np  to mapp the values 1,2,3,4 to rock, paper, scissors, nothing
# you need to put a countdown timer to the game, so the game ends after a number of runs or time period.

class computer_vision:

    def __init__(self, computer_choice, user_choice, no_rounds, choice_list) -> None:
        
        self.computer_choice = computer_choice
        self.user_choice = user_choice
        self.no_rounds = no_rounds
        self.choice_list = choice_list
        self.choice_list = ['rock', 'paper', 'scissors','nothing']

        computer_wins = 0
        user_wins = 0

        pass

    def get_computer_choice(self) -> str:
        """
        this function is used to get the computer choice from rock, paper or scissors
        """
        prediction = self.prediction()
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])
        return self.computer_choice

        pass

    def get_prediction(self):
        model = load_model('keras_model.h5')
    
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
            print( "It's a tie!")
        elif self.computer_choice == 'rock':
            if self.user_choice == 'paper':
                print(f"{self.user_choice} beats {self.computer_choice}, You win!")
            else:
                print( "You lose!")
        elif self.computer_choice == 'paper':
            if self.user_choice == 'scissors':
                print("You win!")
            else:
                print("You lose!")
        elif self.computer_choice == 'scissors':
            if self.user_choice == "rock":
                print("You win!")
            else:
               print("You lose!")
        # no condition true
        else: 
            print( "You have entered an invalid input")

        pass

def play(self):

    
    game = computer_vision(self.computer_choice, self.user_choice, self.no_rounds, self.choice_list)
        
            
    
        

if __name__ == '__main__':
    play(computer_choice, user_choice)


        