import time

lst = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]


def board():
    for i in list(range(3)):
        for j in list(range(3)):
            lst[i][j] = '_'
    for i in list(range(3)):
        for j in list(range(3)):
            print(lst[i][j], end='|')
        print()
    print()


def logic():
    count = 0
    # row=0
    # col=0
    while (True):
        count = count + 1
        # Player 1
        print("Player 1's turn")
        try:
            row = int(input("Row: ")) - 1
            if row > 2 or row < 0:
                raise Exception
        except:
            print("Invalid Row\nThe Row should be 1, 2 or 3")
            try:
                row = int(input("Row: ")) - 1
                if row > 2 or row < 0:
                    raise Exception
            except:
                print("Invalid Row Again\nThe Row should be 1, 2 or 3")
                try:
                    row = int(input("Row: ")) - 1
                    if row > 2 or row < 0:
                        raise Exception
                except:
                    print("Sorry you are not eligible for this game")
                    break
        try:
            col = int(input("Column: ")) - 1
            if col > 2 or col < 0:
                raise Exception
        except:
            print("Invalid Column\nThe Column should be 1, 2 or 3")
            try:
                col = int(input("Column: ")) - 1
                if col > 2 or col < 0:
                    raise Exception
            except:
                print("Invalid Column Again\nThe Column Should be 1, 2 or 3")
                try:
                    col = int(input("Column: ")) - 1
                    if col > 2 or col < 0:
                        raise Exception
                except:
                    print("Sorry you are not eligible to play this game")
                    break
        print()
        if lst[row][col] == 'O' or lst[row][col] == 'X':
            print("Don't Cheat")
            print()
            print("STARTING THE GAME AGAIN.....")
            time.sleep(4)
            print()
            board()
            logic()
            break
        else:
            lst[row][col] = 'O'
        for i in list(range(3)):
            for j in list(range(3)):
                print(lst[i][j], end='|')
            print()
        print()
        if lst[0][0] == 'O' and lst[0][1] == 'O' and lst[0][2] == 'O':
            print("Player 1 Wins")
            break
        elif lst[1][0] == 'O' and lst[1][1] == 'O' and lst[1][2] == 'O':
            print("Player 1 Wins")
            break
        elif lst[2][0] == 'O' and lst[2][1] == 'O' and lst[2][2] == 'O':
            print("Player 1 Wins")
            break
        elif lst[0][0] == 'O' and lst[1][0] == 'O' and lst[2][0] == 'O':
            print("Player 1 Wins")
            break
        elif lst[0][1] == 'O' and lst[1][1] == 'O' and lst[2][1] == 'O':
            print("Player 1 Wins")
            break
        elif lst[0][2] == 'O' and lst[1][2] == 'O' and lst[2][2] == 'O':
            print("Player 1 Wins")
            break
        elif lst[0][0] == 'O' and lst[1][1] == 'O' and lst[2][2] == 'O':
            print("Player 1 Wins")
            break
        elif lst[0][2] == 'O' and lst[1][1] == 'O' and lst[2][0] == 'O':
            print("Player 1 Wins")
            break
        elif count == 5:
            print("Match is Draw, Play Again....")
            print()
            break
        # Player 2
        print("Player 2's turn")
        try:
            row = int(input("Row: ")) - 1
            if row > 2 or row < 0:
                raise Exception
        except:
            print("Invalid Row")
            try:
                row = int(input("Row: ")) - 1
                if row > 2 or row < 0:
                    raise Exception
            except:
                print("Invalid Row Again")
                try:
                    row = int(input("Row: ")) - 1
                    if row > 2 or row < 0:
                        raise Exception
                except:
                    print("Sorry you are not eligible for this game")
                    break
        try:
            col = int(input("Column: ")) - 1
            if col > 2 or col < 0:
                raise Exception
        except:
            print("Invalid Column")
            try:
                col = int(input("Column: ")) - 1
                if col > 2 or col < 0:
                    raise Exception
            except:
                print("Invalid Column Again")
                try:
                    col = int(input("Column: ")) - 1
                    if col > 2 or col < 0:
                        raise Exception
                except:
                    print("Sorry you are not eligible to play this game")
                    break
        print()
        if lst[row][col] == 'O' or lst[row][col] == 'X':
            print("Don't Cheat")
            print()
            print("STARTING THE GAME AGAIN.....")
            time.sleep(4)
            print()
            board()
            logic()
            break
        else:
            lst[row][col] = 'X'
        for i in list(range(3)):
            for j in list(range(3)):
                print(lst[i][j], end='|')
            print()
        print()
        if lst[0][0] == 'X' and lst[0][1] == 'X' and lst[0][2] == 'X':
            print("Player 2 Wins")
            break
        elif lst[1][0] == 'X' and lst[1][1] == 'X' and lst[1][2] == 'X':
            print("Player 2 Wins")
            break
        elif lst[2][0] == 'X' and lst[2][1] == 'X' and lst[2][2] == 'X':
            print("Player 2 Wins")
            break
        elif lst[0][0] == 'X' and lst[1][0] == 'X' and lst[2][0] == 'X':
            print("Player 2 Wins")
            break
        elif lst[0][1] == 'X' and lst[1][1] == 'X' and lst[2][1] == 'X':
            print("Player 2 Wins")
            break
        elif lst[0][2] == 'X' and lst[1][2] == 'X' and lst[2][2] == 'X':
            print("Player 2 Wins")
            break
        elif lst[0][0] == 'X' and lst[1][1] == 'X' and lst[2][2] == 'X':
            print("Player 2 Wins")
            break
        elif lst[0][2] == 'X' and lst[1][1] == 'X' and lst[2][0] == 'X':
            print("Player 2 Wins")
            break


print("**********TIC TAC TOE BOARD GAME**********")
board()
logic()