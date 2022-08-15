
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

    def __init__(self):
        
        self.computer_choice = computer_choice
        self.user_choice = user_choice
        self.no_rounds = no_rounds
        self.choice_list = choice_list
        self.user_score = 0
        self.computer_score = 0

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
        
        self.user_entry = input("Please enter your choice (rock, paper or scissors):")

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
                print(f"Your {self.user_choice} beats computer's {self.computer_choice}, You won this round!")
                self.user_score += 1
               
            else:
                print(f"Computer's {self.computer_choice} beats your {self.user_choice}, You lost this round!")   
                self.computer_score += 1
               

        elif self.computer_choice == 'paper':
            if self.user_choice == 'scissors':
                print(f"Your {self.user_choice} beats computer's {self.computer_choice}, You won this round!")
                self.user_score += 1
             
            else:
                print(f"Computer's {self.computer_choice} beats your {self.user_choice}, You lost this round!")
                self.computer_score += 1
                

        elif self.computer_choice == 'scissors':
            if self.user_choice == "rock":

                print(f"Your {self.user_choice} beats computer's {self.computer_choice}, You won this round!")
                self.user_score += 1
                
            else:
               print(f"Computer's {self.computer_choice} beats your {self.user_choice}, You lost this round!")
               self.computer_score += 1
               
        # no condition true
        else: 
            print( "You have entered an invalid input")

        
        pass

      
      
        

def play(choice_list):
    """
    this function is used to play the game
    """
    
    game = computer_vision()
    game.get_computer_choice()
    game.get_user_choice()
    game.get_winner()

   


    pass

        
            
  

if __name__ == '__main__':
    choice_list = ['rock', 'paper', 'scissors','nothing']
    no_rounds = 5
    computer_choice = ''
    user_choice = ''
    for i in range(no_rounds):
        play(choice_list)
        # delay for 2 milliseconds
        time.time()
        # destroy all the windows
        cv2.destroyAllWindows()
        time.time()

        print("\n")

    

        
    
    
