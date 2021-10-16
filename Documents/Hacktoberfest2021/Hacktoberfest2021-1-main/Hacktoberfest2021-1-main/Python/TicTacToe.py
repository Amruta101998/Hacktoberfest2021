# ● You now know enough to create a real program!
# ● For your first silver project you will create a Tic Tac Toe game for 2 human players.
# ● Let’s describe what the game will be like...
# ● 2 players should be able to play the game (both sitting at the same computer)
# ● The board should be printed out every time a player makes a move
# ● You should be able to accept input of the player position and then place a symbol on the
# board
# ● Creating your first full program is always a big leap, but you will come out the other end a
# much better programmer!
# ● We’ve set up a walkthrough notebook for you to help guide you along with the functions
# you will need to create.
# ● Let’s explore what the game will look like once it is done
# ● We’ll also cover a few useful functions and go through the walkthrough notebook.
# ● Let’s get started!
# Solution Steps:
# ● We need to print a board.
# ● Take in player input.
# ● Place their input on the board.
# ● Check if the game is won,tied, lost, or ongoing.
# ● Repeat b to d until the game has been won or tied.
# ● Ask if players want to play again.
# Step 1 : Write a function that can print out a board. Set up your board as a list, where each index
# 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
# Step 2 :Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think
# about using while loops to continually ask until you get a correct answer.
# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired
# position (number 1-9) and assigns it to the board.
# Step 4: Write a function that takes in a board, along with marker and checks to see if someone
# has won.
# Step 5: Write a function that uses the random module to randomly decide which player goes first.
# You may want to lookup random.randint() Return a string of which player went first.
# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely
# available.
# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full,
# False otherwise.
# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the
# function from step 6 to check if its a free position. If it is, then return the position for later use.
# Step 9: Write a function that asks the player if they want to play again and returns a boolean True
# if they do want to play again.
# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the
# game!

import random 

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('---------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('---------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == "O"):
        marker = input("Enter a Marker X/O for player one : ").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position] = marker


def win_check(board,marker):
    
    if( (board[7]==marker and board[8]==marker and board[9]==marker) or
        (board[4]==marker and board[5]==marker and board[6]==marker) or
        (board[1]==marker and board[2]==marker and board[3]==marker) or
        (board[7]==marker and board[4]==marker and board[1]==marker) or
        (board[8]==marker and board[5]==marker and board[2]==marker) or
        (board[9]==marker and board[6]==marker and board[3]==marker) or
        (board[7]==marker and board[5]==marker and board[3]==marker) or
        (board[9]==marker and board[5]==marker and board[1]==marker)):
        return True
    else:
        return False

def choose_first():
    num = random.randint(0,1)
    
    if num == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def players_choice(board):
    position = 0
    
    while not position in [1,2,3,4,5,6,7,8,9] or not space_check(board,position) : 
        position = int(input("Enter your next position : "))
        
    return position



def replay():
    return input("Do you want to play again (Y/N) : ").lower().startswith('y')

# Here Comes the final Assembly of the game 


while True:
    
    board = [' ']* 10
    
    
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    
    print(turn + " Will play First")
    
    play_game = input("Are you ready to play the game Y/N").lower().startswith('y')
    
    if play_game:
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            # Game logic starts here for player 1 
            
            display_board(board)
            position = players_choice(board)
            place_marker(board,player1_marker,position)
            
            if win_check(board,player1_marker):
                display_board(board)
                print("Player 1 Won the game!! congratzz")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The Game is Draw, Better luck next time !!')
                    break
                else:
                    turn = "Player 2"
        else:
            # Player 2 Logic 
            
            display_board(board)
            position = players_choice(board)
            place_marker(board,player2_marker,position)
            
            if win_check(board,player2_marker):
                display_board(board)
                print("Player 2 Won the game!! congratzz")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The Game is Draw, Better luck next time !!')
                    break
                else:
                    turn = "Player 1"
    
    if not replay():
        break