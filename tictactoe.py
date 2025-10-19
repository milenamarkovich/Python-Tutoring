import os

# First, we want to define our helper functions:
def draw_board(spots):
    # Write code that uses the value of the spots dictionary to print the board
    pass

def check_turn(turn):
    # Write code that check who's turn it is 
    # Hint: if we have Player 1 and Player 2, how can we differentiate between the two numbers - 1 and 2?
    pass

def check_for_win(spots):
    # We have three winning cases:
    # First, let's check the horizontal:
    
    # Next, the vertical
    
    # And lastly the diagonal
    pass

spots = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}

# Set a variable that tracks whether we are still playing

# Set a variable that tracks whose turn it is

# Set a variable to track the previous turn (this will help us notify the user when they set an invalid number)

# Set a variable to track whether the game is complete (this will help us track when someone has won the game)

# Create a loop for our game (i.e. while we continue playing)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    # Check if the user has entered an invalid number (i.e. if we are stuck on the same turn)
    
    # Iterate to the next turn

    # print(f"Player {(turn%2)+1}'s turn: Pick your spot or press 'q' to quit")
    
    # Get user choice as a keyboard input

    # Set condition such that if the user has input 'q', we quit the game

    # Set condition such that if user input is valid (i.e. it is a digit and in our board) we then check if 
    # the input is an available spot (i.e. it is not currently occupied by an 'X' or '0'). Then make sure to iterate to the next turn
    # and set the users choice as their symbol on the board.
    
    # Check for win condition - if someone has won, ensure to set playing to False, and complete to True

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

# Print the results if the game is complete. Remember that the turn variable will be set to the most recent player's turn, aka 
# the winner. Check whether this turn corresponds to 'X' or '0'. If neither, we have a tie!
      
