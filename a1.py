#!/usr/bin/env python3
###################################################################
#
#   CSSE1001/7030 - Assignment 1
#
#   Student Username: s4448451
#
#   Student Name: Matthew Wing-Heng Yau
#
###################################################################

###################################################################
#
# The following is support code. DO NOT CHANGE.

from a1_support import *

# End of support code
################################################################

# Write your code here


def get_position_in_direction(position, direction):
    """takes a row, column pair representing a position,
    and a direction character and returns the position
    of the adjacent square in given direction.

    get_position_in_direction(str, str) -> str
    """
    x,y = position
    if direction == 'e':
        y += 1      
    elif direction == 's':
        x += 1
    elif direction == 'n': 
        x -= 1
    elif direction == 'w':
        y -= 1                     
    return (x,y)



def interact():
    """Request user input, check input and acts upon user input  

    interact() -> None
     
    """
    maze_input = input('Enter maze file: ')
    new_maze = load_maze(maze_input)

    current_pos = START_POSITION #Set position to (1,1)
    print("") 
    print_maze(new_maze, START_POSITION)
    print("")
    
    blist = []
    game_on = True #for terminating the game
    game_win = False
    game_lose = False
    while game_on:
        user_input = input("Command: ").strip()
    
        if user_input == "?":
            print(HELP_TEXT)
            
        elif user_input in DIRECTIONS: 
            new_pos, new_char = move(new_maze, current_pos, user_input)
            #Saves potential new position and potential new character
            if new_char != "#": 
                blist.append(current_pos) #track previous position
                current_pos = new_pos #update current position
                if new_char in BAD_POKEMON:
                    game_lose = True
                elif new_char in GOOD_POKEMON:
                    game_win = True
                
            else:
                print("You can't go in that direction.")
             
        elif user_input == "r":
            blist = [] 
            current_pos = START_POSITION #Reset history
        elif user_input == "b":
            if len(blist) == 0: #if list is empty print error message
                print('You cannot go back from the beginning.')
            else: #if list not empty go back one space
                current_pos = blist[-1]
                blist.pop()
        elif user_input == "p":
            legal_dir = ", ".join(get_legal_directions(new_maze,current_pos))
            #get allow directions, join result in string
            print('Possible direction: ' + legal_dir)
        elif user_input == "q": 
            q_user_input = input('Are you sure you want to quit? [y] or n: ')
            if q_user_input != "n":
                game_on = False #End while loop                        
        else:
            print('Invalid command: '+ user_input)
        
        if game_win:
            print (WIN_TEXT.replace("{}", POKEMON[new_char])) #Replace filler with Pokemon
            game_on = False
        elif game_lose:
            print (LOSE_TEXT.replace("{}", POKEMON[new_char])) #Replace filler with Pokemon
            game_on = False
        elif game_on == True:
            print("")
            print_maze(new_maze, current_pos)
            print("")
            



def print_maze(maze, position):
    """takes a maze string and the position of the player,
    and prints the maze with the player shown as an 'A'.

    print_maze(str,str) -> str
    """
    maze.replace(PLAYER," ")
    m_index = position_to_index(position, maze_columns(maze))
    maze = maze[:m_index] +PLAYER + maze[m_index+1:]
    print(maze)
    
    
def move(maze, position, direction):
    """Takes a maze string, a position of a square and a direction and
    returns a pair of the form (position, square) where position is the
    position after move and sqaure is the resulting square after the move.

    move(str, str, str) -> (tuple(int,int), str)

    """
    if direction not in get_legal_directions(maze,position): 
        new_pos = position #return original value
    else:
        new_pos = get_position_in_direction(position, direction)
    
    new_char = maze[position_to_index(get_position_in_direction(position, direction), maze_columns(maze))]
    # Find a character at a specific position in the maze by finding new position and convert it into a index value
    return (new_pos, new_char)

    

def get_legal_directions(maze,position):
    """Takes a maze string and a position, and returns a list of
    legal directions for that square.

    get_legal_directions(str,tuple(int,int)) -> list
    """
    legal_dir = []
    for i in DIRECTION_DELTAS:
        get_pos = get_position_in_direction(position, i) 
        maze_pos = maze[position_to_index(get_pos,maze_columns(maze))]
        if maze_pos == " " or maze_pos in POKEMON: #If it is a pokemon or space it is a legal move
            legal_dir.append(i) #add legal move to list
    return legal_dir
        
        

    
    
    
    


##################################################
# !!!!!! Do not change (or add to) the code below !!!!!
# 
# This code will run the interact function if
# you use Run -> Run Module  (F5)
# Because of this we have supplied a "stub" definition
# for interact above so that you won't get an undefined
# error when you are writing and testing your other functions.
# When you are ready please change the definition of interact above.
###################################################

if __name__ == '__main__':
    interact()
