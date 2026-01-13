# importing libraries
import pygame
import time
import random

# Set the snake speed - how fast can it move?
snake_speed = 2

# Set the display window size
# Window size
window_x = 720
window_y = 480

# Define some colors
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('<-- Snake Game Name -->')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Set a default position for the snake
snake_position = [50,240]

# Define first 4 blocks of snake body (let's say each block is 10x10 pixels)
snake_body = [[50,240], [40,240],[30,240]]

# Generate a random starting position for the apple which the snake will try to eat
# Note: Remember that the apple must appear within the window boundaries and at a position that the snake can reach (i.e. the snake is 10x10 pixels)
apple_position = [random.randint(0,window_x//10 * 10),random.randint(0,window_y//10 * 10)]

apple_spawn = True

# Set default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# Start from score of 0
score = 0

# displaying Score function
def show_score(choice, color, font, size):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():
  
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after 2 seconds we will quit the program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()


# Main Function
while True:
    
    # Create logic for key events (i.e. user presses arrow keys to move the snake: 'UP', 'DOWN', 'LEFT', 'RIGHT')
    # Hint: You can use pygame.KEYDOWN event to detect key presses
    # Hint 2: You can use pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT to detect specific arrow key presses
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to ='UP'
            if event.key == pygame.K_DOWN: 
                change_to ='DOWN' 
            if event.key == pygame.K_RIGHT:
                change_to ='RIGHT'
            if event.key == pygame.K_LEFT: 
                change_to ='LEFT'# Replace with your code to handle key events

    # If two keys pressed simultaneously we don't want snake to move into two directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Create logic to move the snake in the specified direction - remember the snake moves by 10 pixels in each direction
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10 # Replace with your code to move down
    if direction == 'LEFT':
        snake_position[0] -= 10 # Replace with your code to move left
    if direction == 'RIGHT':
        snake_position[0] += 10 # Replace with your code to move right

    # Snake body growing mechanism - if apples and snakes collide then scores will be incremented by 10
    # Hint: Use .insert() method to add block of length snake_position to the snake_body list
    snake_body.insert(0,list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        apple_spawn = False
        score += 1
    else:
        snake_body.pop()

    # Check if the snake has eaten the apple - if the snake has eaten the apple, then the head of the snake (snake_position) will be equal to the apple (apple_position)
    # If they are equal, increase the score by 10 and set apple_spawn to False (to indicate that we need to spawn a new apple)
    # Else, remove the last block of the snake body using .pop() method - this makes the snake move forward without growing the body
    # Your code here
        
    # Spawn a new apple if apple_spawn is False and set apple_spawn to True
    # After spawning the apple, make sure to set game_window.fill(black) to refresh the game window
    # Your code here

    if apple_spawn == False:
        apple_position = [random.randint(0,window_x//10 * 10),random.randint(0,window_y//10 * 10)]
    
    apple_spawn = True
    game_window.fill(black)
   
    
    # Draw the snake and apple on the game window
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        apple_position[0], apple_position[1], 10, 10))

    # I.e. First, check if the snake has hit the boundaries of the window
    # Your code here
    if snake_position[1] < 0 or snake_position[0] < 0 or snake_position[1] > window_y or snake_position[0] > window_x:
        game_over()
    # Second, check if the snake has hit itself - loop through each block in the snake_body list (except the head) and check if the head's position is equal to any block's position
    # Your code here

    # If any of the game over conditions are met, call the game_over() function

    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
