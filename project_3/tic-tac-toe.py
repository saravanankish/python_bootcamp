import random

print("Let's Play Tic Tac Toe!\nEnter Players names")
players = [input("Player 1: ").capitalize(), input("Player 2: ").capitalize()]  # Gets User names
history = {players[0]: 0,
           players[1]: 0}  # Creates a history dictionary to store number of games won by both the players


# Is used to display the board
def display(tictac):
    print(f'''
                            POSITIONS
    {tictac[7]}|{tictac[8]}|{tictac[9]}             7 | 8 | 9
    ---+---+---            ---+---+---
    {tictac[4]}|{tictac[5]}|{tictac[6]}     =>      4 | 5 | 6
    ---+---+---            ---+---+---
    {tictac[1]}|{tictac[2]}|{tictac[3]}             1 | 2 | 3
''')


# Checks the input is valid or not
def valid_input():
    while True:
        pos = input("Enter the Position: ")
        if pos != " ":
            if pos.isdigit():
                if int(pos) in range(1, 10):
                    return int(pos)
                print('Not a valid Position')
            else:
                print('Enter numbers between 1-9')
                continue
        else:
            print('Thank You for playing Tic Tac Toe!')
            exit(0)


# Checks whether the position is valid or not and puts "X" or "O" at a valid position user gives
def valid_pos(turn, tictac, symbol_player):
    print(f'{turn} chance')
    pos = valid_input()
    while True:
        if tictac[pos] == '   ':
            tictac[pos] = ' ' + dict(symbol_player)[turn] + ' '
            display(tictac)
            break
        else:
            print('Cannot overwrite, Please select empty location')
            pos = valid_input()


# Check whether a player won or not
def check_win(tictac):
    check = 0
    if tictac[1] == tictac[2] == tictac[3] != '   ' or tictac[4] == tictac[5] == tictac[6] != '   ' or tictac[7] == \
            tictac[8] == tictac[9] != '   ':
        check = 1
    elif tictac[1] == tictac[4] == tictac[7] != '   ' or tictac[2] == tictac[5] == tictac[8] != '   ' or tictac[3] == \
            tictac[6] == tictac[9] != '   ':
        check = 1
    elif tictac[1] == tictac[5] == tictac[9] != '   ' or tictac[3] == tictac[5] == tictac[7] != '   ':
        check = 1
    return check


# Game flow Takes place
def game(tictac, symbol, symbol_player):
    sym1, sym2 = symbol[random.randint(0, 1)]     # Randomly generates the turn of the user
    turns = 0 if sym1 == 'X' else 1
    print(f"{symbol_player[turns][0]} is playing first")
    display(tictac)
    for i in range(9):
        if not i % 2:
            turn = symbol_player[turns][0]
            valid_pos(turn, tictac, symbol_player)
        else:
            turn = symbol_player[not turns][0]
            valid_pos(turn, tictac, symbol_player)
        if i >= 4:
            if check_win(tictac):
                display(tictac)
                history[turn] += 1
                print(f"{turn} WON ")
                break
        if i == 8:
            print("That's a Tie")


def main():
    symbol = [('O', 'X'), ('X', 'O')]
    while True:
        tictac = ['', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']          # The Tic Tac Toe Board
        print("\nLet's Start the Game!")
        random_num = random.randint(0, 1)                      # Gets a random number to randomly select marker for the two players
        symbol_player = [(players[random_num], 'X'), (players[not random_num], 'O')]     # Randomly selects the marker for the two player
        print(f"{players[random_num]} is X and {players[not random_num]} is O")          # Displays the marker for the player
        game(tictac, symbol, symbol_player)
        print(f"{players[0]} has won {history[players[0]]} and {players[1]} has won {history[players[1]]} so far\n")     # Prints the history of the game for the current session
        if input("Play Again? (Y to continue): ").lower() != "y":                    # Asks user whether play again or quit
            print(
                f"{players[0]} has won {history[players[0]]} and {players[1]} has won {history[players[1]]}\nSee You Again :)")

            exit(0)


if __name__ == '__main__':
    main()
