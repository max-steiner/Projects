import time
import sys
import random


# The function demonstrate the rules of the game; in case of refusal to continue the game, it provides a logout
def lets_play():
    print()
    print('''Let's play the game "TIC-TAC-TOE" (©Max M.Steiner LTD, Ashdod-city).\n
Тhe player's task - is to place a TIC marks ("0") or a TAC marks ("╳") in a full row.
The player, who does it first, wins. Time to think over the each move isn't more than 20 seconds\n''')
    answer = int(input('''DISCLAMER: Attention! The game can make you addictive. In the event of a hallucination 
           during the game, dizziness or overwork, immediately, call for help.
           ____________________
           If you want to play - press "1" and ENTER. If you don't want - press "0" and ENTER: '''))
    while answer not in [1, 2]:
        print("Incorrect data entry.")
        answer = int(input('''If you want to play - press "1" and ENTER. If you don't want - press "0" and ENTER: '''))
    if answer == 1:
        print('\n' * 100)
    else:
        print('\n')
        print("GOOD BY WORLD!!!)))")
        sys.exit()


# The function for choosing one option of the game from the two offered.
def make_choice():
    choice_game = int(input('''Choose a game options:\n
                        Press "1" and ENTER if you want to play with artificial intelligence "X" on the board 3x3.
                        Press "2" and ENTER if you want to play with yourself or with your friend on the board 4x4.\n
                        __________________________
                        Game options: '''))
    while choice_game not in [1, 2]:
        choice_game = int(input('''Incorrect data entry.\n
                               Press "1" and ENTER if you want to play with artificial intelligence "X" on board 3x3.\n
                               Press "2" and ENTER if you want to play with your friend on a board 4x4.\n
                               __________________________
                                Game options: '''))
    if choice_game == 1:
        size = 3
    else:
        size = 4
    return size


# The function displays the playing board in 2 versions 3 x 3 or 4 X 4.
# This function also saves the progress of the game in the list/
def take_gameboard(num_square, size=3):
    if size == 3:
        print("■□" * 8)
        for n in range(size):
            print(" ┇", num_square[n * 3], "┇", num_square[(n * 3) + 1], "┇", num_square[(n * 3) + 2], "┇", sep=" ")
            print("__" * 8)
        print("■□" * 8)
    else:
        print("■□" * 14)
        for n in range(size):
            print(" ┇", num_square[n * size], "┇", num_square[n * size + 1], "┇", num_square[n * size + 2], "┇",
                  num_square[n * size + 3], "┇", sep="  ")
            print("__" * 14)
        print("■□" * 14)


# This function ensures the game of a person against a bot. It used only on the playing field 3 X 3/
# People always move with "0".
def make_move_3(num_square):
    start_time = time.time()
    num_square_old = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    move = int(input("Please make your move. Input the number of square (1 - 9) and press ENTER: "))
    while move not in num_square_old:
        print("Input Error. Enter correct data")
        move = int(input("Please make your move. Input the number of square (1 - 9) and press ENTER: "))
    while (num_square[move - 1]) not in num_square_old:
        print(''' \¯\_(ツ)_/¯ This square is already taken.''')
        move = int(input("Please make your move. Input the number of square (1 - 9) and press ENTER: "))
    if time.time() - start_time > 60:
        return False
    else:
        num_square[move - 1] = "0"
        return num_square


#This function is designed for 2 people playing on a board 4 x 4.
#The function also provides a fixation of the time for thinking about the move.
def make_move_4(num_square, num_move):
    start_time = time.time()
    num_square_old = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    move = int(input("Please make your move. Input the number of square (1 - 9) and press ENTER: "))
    while move not in num_square_old:
        print("Input Error. Enter correct data")
        move = int(input("Please make your move. Input the number of square (1 - 9) and press ENTER: "))
    while (num_square[move - 1]) not in num_square_old:
        print(''' \¯\_(ツ)_/¯ This square is already taken.''')
        move = int(input("Please make your move. Input the number of square (1 - 9) and press ENTER: "))
    if time.time() - start_time > 20:
        return False
    else:
        if num_move % 2 == 0:
            num_square[move - 1] = "0"
        else:
            num_square[move - 1] = "X"
    return num_square


#The function is designed to determine winning combinations on the boards 3 x 3 and 4 x 4.
#In case of a winning combination, the function returns False, otherwise the function returns True.
#The function iterates the list, containing all possible winning combinations.
def identify_win(num_square, size=3):
    win_pos_3 = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    win_pos_4 = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16), (1, 3, 9, 13),
                 (2, 6, 10, 14), (3, 7, 11, 15), (4, 8, 12, 16), (1, 6, 11, 16), (4, 7, 10, 13)]
    if size == 3:
        for row in win_pos_3:
            if (num_square[row[0] - 1]) == (num_square[row[1] - 1]) == (num_square[row[2] - 1]):
                return False
        return True
    else:
        for row in win_pos_4:
            if (num_square[row[0] - 1]) == (num_square[row[1] - 1]) == (num_square[row[2] - 1]) == (num_square[row[3] - 1]):
                return False
        return True


#The bot for playing a person with a computer on a board of 3 x 3.
#At first, it looks through all its own winning combinations (pre_win_pos).
#If they are absent, bot looks through the opponent's winning combinations and blocks it.
def launch_bot(num_square, num_move):
    pre_win_pos = [(1, 2), (2, 3), (1, 3), (4, 5), (5, 6), (4, 6), (7, 8), (8, 9), (7, 9), (1, 4), (4, 7), (1, 7),
                     (2, 5), (5, 8), (2, 8), (3, 6), (6, 9), (3, 9), (1, 5), (5, 9), (1, 9), (3, 5), (5, 7), (3, 7)]
    move_win = [3, 1, 2, 6, 4, 5, 9, 7, 8, 7, 1, 4, 8, 2, 5, 9, 3, 6, 9, 1, 5, 7, 3, 5] #implamentation of pre_winning position
    num_square_old = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst_corners = [0, 2, 6, 8]
    if num_move <= 3: #Bot always makes the first two moves to the corners of the play board.
        move_bot = lst_corners[random.randint(0, 3)]
        if num_square[move_bot] in num_square_old:
            num_square[move_bot] = "X"
        else:
            while num_square[move_bot] not in num_square_old:
                move_bot = lst_corners[random.randint(0, 3)]
                if num_square[move_bot] in num_square_old:
                    num_square[move_bot] = "X"
                    break
    if num_move > 3: #starting from moves 4 the bot looks through pre_winning position
        for i, j in enumerate(pre_win_pos):
            a, b = j[0], j[1] #The helper local variables for shortening the string
            c = move_win[i]
            if [num_square[a - 1], num_square[b - 1]] == ["X", "X"] and num_square[c - 1] in num_square_old:
                num_square[c - 1] = "X"
                break
            elif [num_square[a - 1], num_square[b - 1]] == ["0", "0"] and num_square[c - 1] in num_square_old:
                num_square[c - 1] = "X"
                break
            else:
                for a in num_square:
                    if a in num_square_old:
                        a = "X"
                    break
    return num_square

#This function consists of 2 main loops: 1-t provides a game of a person with a computer on the board 3 x 3.
#The 2-d loop provides a game of 2 people on a board 4 x 4.
def main():
    lets_play()
    size = make_choice() #this variable sets the size of the playing board
    print('\n' * 100) #simulation of screen cleaning
    num_square = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16][:(size ** 2)] #play board
    num_move = 0
    if size == 3: # THR FIRST MAIN LOOP
        take_gameboard(num_square, size=3)
        while identify_win(num_square, size=3) is True and num_move != 9:
            num_move += 1 #counter of moves
            num_square = launch_bot(num_square, num_move)
            print('\n' * 100)
            take_gameboard(num_square, size=3)
            if num_move == 9:
                break
            print(f"The move # {num_move}")
            if identify_win(num_square, size=3) is False:
                break
            print("\nThe artificial intelligence made its move.")
            num_move += 1
            num_square = make_move_3(num_square)
            print(f"The move # {num_move}")
            if num_square is False: #in a case of exceeding the time to think about a move
                print("\nYou have been thinking too much. The game is over")
                sys.exit()
            print('\n')
            take_gameboard(num_square, size=3)
            if num_move == 9:
                break
            if identify_win(num_square, size=3) is False:
                break
        print('\n')
        take_gameboard(num_square, size)
        if identify_win(num_square, size=3) is False and num_move % 2 != 0:
            print()
            print('''The victory was won by artificial intelligence.\n      
                                Do you have a "bagrut" ???
                                        ٩(｡•́‿•̀｡)۶''')
        elif identify_win(num_square, size=3) is False and num_move % 2 == 0:
            print('n' * 100)
            print('''Congratulations on the victory. You beat the computer. Your IQ is at least 40 points.''')
        elif identify_win(num_square, size=3) is True and num_move == 9:
            print()
            print('''It seems we are at an impasse. The game ended in a DRAW''')
    else:
        take_gameboard(num_square, size=4)  #THE SECOND MAIN LOOP
        while num_move <= 16:
            num_move += 1
            print(f"Move # {num_move}")
            print(f"The move {'X' if num_move % 2 != 0 else '0'}:")
            num_square = make_move_4(num_square, num_move)
            print('\n' * 100)
            if num_square is False:
                print("\nYou have been thinking too much. The game is over")
                sys.exit()
            take_gameboard(num_square, size=4)
            if identify_win(num_square, size=4) is False:
                break
        if identify_win(num_square, size=4) is False:
            print(f"Won the {'X' if num_move % 2 != 0 else '0'}")
        else:
            print("The game ended in a DRAW")


main()
