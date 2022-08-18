# Computer-Vision-Rock-Paper-Scissors
## Milestone 1
- An image project model for classifying four different classes "Rock", "paper", "Scissors", and "Nothing" using a "Teachable-Machine", an open source image model creation site.
- The model is downloaded, which includes two files "keras_model.h5" and "labels.txt", the former containing the structure and parameters of the deep learning model built and the later housing information on the labels which are the classes the model was built to identify.

## Milestone 2
- The dependencies for the project are installed in an environment called "my_env", making use of conda.
- Extra steps are required for apple M1/M2 laptops to enable tensorflow to run.  The steps [here](https://www.mrdbourke.com/setup-apple-m1-pro-and-m1-max-for-machine-learning-and-data-science/) are followed.

## Milestone 3
- The functions that get the computer choice and user choice (rock, paper scissors or nothing) are created, named get_computer_choice and get_user_choice respectively
- Making use of if else statements, the method that defines and displays the winner is implemented.
- This function is also within the game class and therefore a method of that class.

## Milestone 4
- An instance of the computer vision class is created, called "game"
- Then a function called "play" is created, which calls the methods of the class to get the computer choice and the user choice, and then calls the method that defines and displays the winner when called.
- Two varibales are added to the instance of the class : computer_wins and the user_wins, each set to 0.
- A function named "get_winner" is created, which is used to determine the winner of the game. It makes use of if else statements to determine the winner of the game making use of the computer choice and user choice.
- The get_winner function returns the computer and user wins.
- To ensure the game stops when either player gets three points, a while loop is created that runs until either player gets three points.
```python
  game = computer_vision(computer_wins=0, user_wins=0)
    game.get_winner()
    while game.user_wins < 3 and game.computer_wins < 3: 
```

## Milestone 5

