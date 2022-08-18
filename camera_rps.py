
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

    def __init__(self,computer_wins = 0, user_wins = 0):
        
        self.computer_choice = computer_choice
        self.user_choice = user_choice
        self.choice_list = choice_list
        self.computer_wins = computer_wins
        self.user_wins = user_wins
       
        

        #computer_wins = 0
        #user_wins = 0

        pass

    def get_computer_choice(self):
        """
        this function is used to get the computer choice from rock, paper or scissors
        """
        #prediction = self.prediction()
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])

        pass

    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        
        self.user_entry = input("Please show your choice by hand (rock, paper or scissors) and press enter to continue:")
        

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)

            # user choice should be gotten from prediction
            
            return np.argmax(prediction)

            cv2.imshow('frame', frame)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
    
        pass


    def get_user_choice(self):
        """
        this function is used to get the user's choice of rock, paper or scissors from prediction function
        """
        # maapping the aregmax values to rock, paper, scissors and nothing
        
        self.user_choice = self.get_prediction()

        if self.user_choice == 0:
            self.user_choice = 'rock'
        elif self.user_choice == 1:
            self.user_choice = 'paper'
        elif self.user_choice == 2:
            self.user_choice = 'scissors'
        else:
            self.user_choice = 'nothing'
            
         

        
    
        pass

   
    def get_winner(self):
        """
        this function is used to get the winner of the game
        """
        

        if self.computer_choice == self.user_choice:
            print( "It's a tie!")
        elif self.computer_choice == 'rock':
            if self.user_choice == 'paper':
                self.user_wins += 1 
                print(f"Your {self.user_choice} beats computer's {self.computer_choice}, You won this round!")
              
               
            else:
                self.computer_wins += 1
                print(f"Computer's {self.computer_choice} beats your {self.user_choice}, You lost this round!") 
                
               

        elif self.computer_choice == 'paper':
            if self.user_choice == 'scissors':
                self.user_wins += 1
                print(f"Your {self.user_choice} beats computer's {self.computer_choice}, You won this round!")
                
             
            else:
                self.computer_wins += 1
                print(f"Computer's {self.computer_choice} beats your {self.user_choice}, You lost this round!")
                
                

        elif self.computer_choice == 'scissors':
            if self.user_choice == "rock":
                self.user_wins += 1
                print(f"Your {self.user_choice} beats computer's {self.computer_choice}, You won this round!")
                
                
                
            else:
                self.computer_wins += 1
                print(f"Computer's {self.computer_choice} beats your {self.user_choice}, You lost this round!")
               
               
        # no condition true
        else: 
            print( "You have entered an invalid input")

        
        return self.computer_wins, self.user_wins

      
      
        

def play(choice_list):
    """
    this function is used to play the game
    """
    
    game = computer_vision(computer_wins=0, user_wins=0)
    # making sure the game runs till either user or computer gets 3 winas
    #while game.user_wins < 3 and game.computer_wins < 3::
 

   
    game.get_winner()
    while game.user_wins < 3 and game.computer_wins < 3: 
        game.get_computer_choice()
        game.get_user_choice()  
        game.get_winner()    
        if game.user_wins == 3:
            print("You have won the game")
            break
        elif game.computer_wins == 3:
            print("Computer has won the game")
            break
        else:
            continue
    

        
    print("\n")
    time.sleep(1)
    print(f"User's score is {game.user_wins} and computer's score is {game.computer_wins}")
    pass


        
            
  

if __name__ == '__main__':
    choice_list = ['rock', 'paper', 'scissors','nothing']
    play(choice_list)
   


    

        
    
    
