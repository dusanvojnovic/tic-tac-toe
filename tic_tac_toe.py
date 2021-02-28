import os 

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board(board):
    print(board[7] + ' |' + board[8] + ' |' + board[9])
    print("--------")
    print(board[4] + ' |' + board[5] + ' |' + board[6])
    print("--------")
    print(board[1] + ' |' + board[2] + ' |' + board[3])


def game():
    play = "X"
    count = 0
    global board
    for i in range(10):
        os.system('cls')
        print ("Welcome to the TicTacToe! Use your num keypad to play.")
        print_board(board)
        
        choice = input(f"Player {play} it's your turn to play: ")
        move = int(choice)

        if board[move] != " ":
            print("That field is not empty, please try again.")
            continue
        else:
            board[move] = play
            count += 1
        
        if count >= 5:
            # checking rows
            if board[7] == board[8] == board[9] == play or \
                board[4] == board[5] == board[6] == play or \
                board[1] == board[2] == board[3] == play:
                os.system('cls')
                print_board(board)
                print (f"GAME OVER! The winner is {play} player!")
                break
                
            # checking columns
            elif board[7] == board[4] == board[1] == play or \
                board[8] == board[5] == board[2] == play or \
                board[9] == board[6] == board[3] == play:
                os.system('cls')
                print_board(board)
                print (f"GAME OVER! The winner is {play} player!")
                break

            # checking diagonals
            elif board[1] == board[5] == board[9] == play or \
                board[7] == board[5] == board[3] == play:
                os.system('cls')
                print_board(board)
                print (f"GAME OVER! The winner is {play} player!")
                break

        if count == 9:
            os.system('cls')
            print_board(board)
            print ("GAME OVER! It's tied!")
            break

        if play == "X":
            play = "O"
        else:
            play = "X"

    if input("Do you want to play again? (Y)es or (N)o: ").upper() == "Y":
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            os.system('cls')
            game()
    else:
        os.system('cls')
        print("Goodbye")
    

game()
        



            