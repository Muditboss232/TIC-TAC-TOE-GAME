print("2 PLAYER TIC-TAC-TOE GAME")
print("In this game you have to ENTER the number, you want to place a X or O on the board")
def tictactoe():
    gameboard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    winningplaces = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(gameboard[0], gameboard[1], gameboard[2])
        print(gameboard[3], gameboard[4], gameboard[5])
        print(gameboard[6], gameboard[7], gameboard[8])
        print()
#This code places a x for player 1 and also if player 1 one enters a place that is already occupied it will tell
#to try again
    def player1():
        n = number()
        if gameboard[n] == "X" or gameboard[n] == "O":
            print("\nYOU CANNOT GO THERE --- TRY AGAIN")
            player1()
        else:
            gameboard[n] = "X"

#And again this is the same thing but here it puts a O for player 2
    def player2():
        n = number()
        if gameboard[n] == "X" or gameboard[n] == "O":
            print("\nYOU CANNOT GO THERE --- TRY AGAIN")
            player2() 
        else:
            gameboard[n] = "O"

    def number():
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nINVALID INPUT ---- TRY AGAIN")
                        continue
                except ValueError:
                   print("\nINVALID INPUT ---- TRY AGAIN")
                   continue


    def check_board():
        count = 0
        for a in winningplaces:
            if gameboard[a[0]] == gameboard[a[1]] == gameboard[a[2]] == "X":
                print("Player 1 Wins!\n")
                return True


            if gameboard[a[0]] == gameboard[a[1]] == gameboard[a[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if gameboard[a] == "X" or gameboard[a] == "O":
                count += 1
            if count == 9:
                print("TIE\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1s TURN")
        player1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 2s TURN ")
        player2()
        print()

    if input("Play again (YES/NO)\n") == "YES":
        print()
        tictactoe()

tictactoe()