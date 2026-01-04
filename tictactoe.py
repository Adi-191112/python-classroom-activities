board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}
board_keys = []
for key in board:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turn = 'x'
    count = 0

    for i in range(10):
        printBoard(board)
        print("it's your turn," + turn + ".move to which place?")

        move = input()

        if board[move] == ' ':
            board[move] = turn
            count = count + 1
        
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ' : 
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif board['4'] == board['5'] == board['6'] != ' ' : 
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif board['1'] == board['2'] == board['3'] != ' ' : 
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break


            elif board['1'] == board['4'] == board['7'] != ' ' : 
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break


            elif board['2'] == board['5'] == board['8'] != ' ' : 
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break


            elif board['3'] == board['6'] == board['9'] != ' ' : 
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif board['7'] == board['5'] == board['3'] != ' ' : 
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break


            elif board['9'] == board['5'] == board['1'] != ' ' : 
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break


            elif board['4'] == board['5'] == board['6'] != ' ' : 
                printBoard(board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break


        if count == 9:
            print("\nGame Over.\n")
            print("its a Tie!!")

        
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'

if __name__ == "__main__":
    game()
        