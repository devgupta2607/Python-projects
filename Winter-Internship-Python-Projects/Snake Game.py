
#importing the modules curses and sys 
import curses,sys

#importing key functions from the curses module to contol snake 
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint  #importing random function 

#initialization of new window/screen to start the game 
sys.__stdout__ = sys.stdout
curses.initscr()
win = curses.newwin(20, 60, 0, 0)  #setting up the boundaries for the play zone

win.keypad(1)  #to activate the keypad to play 
curses.noecho()
curses.curs_set(0)  #used to hide the cursor from the screen

#set the border properties to make border visible
win.border(0)
win.nodelay(1)

key = KEY_RIGHT   # Initializing values (Direction) 
score = 0
snake = [[4,10],[4,9],[4,8]]   # Initial snake co-ordinates 
food= [10,20]  # First food co-ordinates 
win.addch(food[0],food[1],'*')   # Prints the food as * 

while key != 27:   # While Esc key is not pressed 
    win.border(0)

    #this will print the score and the sting SNAKE on the top 
    win.addstr(0,2,'Score : '+ str(score) + ' ')
    win.addstr(0,27, ' Snake ')

    # Increases the speed of Snake as its length increases 
    win.timeout(int(150 - (len(snake)/5 + len(snake)//10)%120))
    prevKey = key   # In case of no change previous key is used 
    event = win.getch()
    key = key if event == -1 else event

    #If SPACE BAR is pressed it will pause/resume the game 
    if key == ord(' '):
        key = -1
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    # If any other key is pressed other than the specified ones then previous key action will take place 
    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN,27]:
        key = prevKey
    # Calculates the new coordinates of the head of the snake to increase the length of snake when snake eats the food 
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    # If snake crosses the boundaries, make it enter from the other side on both x-axis and y-axis 
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1

    # If snake hits itself 
    if snake[0] in snake[1:]: break


    if snake[0] == food:  # When snake eats the food 
        food=[]
        score += 1
        
        # Using the random function to change the coordinates of food and move to the next position 
        while food == []:
            food = [randint(1,18), randint(1,58)]  #food=(y,x) 

            if food in snake: food = []
        win.addch(food[0], food[1], '*')  #set the food coordinates  and food character to show 

    else:
        last = snake.pop()   # If it does not eat the food,  length decreases 

        win.addch(last[0],last[1],' ')

    #set the snake coordinates and snake character to show 
    win.addch(snake[0][0], snake[0][1],'#')

#exits the curses window that we created
curses.endwin()
#Display the Final score on the screen on exit
print("\nGame Over\nYour Score - " + str(score))
#hold the screen until you press enter
input('')






    
