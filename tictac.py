
board = [' ' for x in range(10)]

def boarddraw(board):
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")

def freespaceavliable(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def spaceavilable(pos):
    if board[pos]==" ":
        return True
    else:
        return False

def insertlatter(letter , pos):
    board[pos] = letter

def Winner(board,l):
    if board[1]==board[2]==board[3]==l or board[4]==board[5]==board[6]==l or board[7]==board[8]==board[9]==l or board[1]==board[5]==board[9]==l or board[3]==board[5]==board[7]==l or board[1]==board[4]==board[7]==l or board[2]==board[5]==board[8]==l or board[3]==board[6]==board[9]==l :
        return True
    else:
        return False

def playermove():
    run = True

    while run:
        move = input("Please enter any position to put 'X' from (1-9) : ")
        try:
            move = int(move)
            if move >= 1 and move <= 9 :
                if spaceavilable(move) :
                    insertlatter('X', move)
                    run= False
                else:
                    print("This is space ia already occupied , Try different ")
            else:
                print("Please enter a valid number")



        except:
            print("Please enter a valid number")

def computermove():
    possiblemoves = [x for x,letter in enumerate(board) if letter ==' ' and x!=0]
    move = 0
    for step in ['O','X']:
        for i in possiblemoves:
            boardcopy =board[:]
            boardcopy[i] = step
            if Winner(boardcopy,step):
                move=i
                return move

    corner=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            corner.append(i)

    if len(corner)>0:
        move = selectrandom(corner)
        return move

    if 5 in possiblemoves:
        move = 5
        return move
    edges = []
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edges.append(i)

    if len(edges)>0:
        move = selectrandom(edges)
        return move

def selectrandom( avlib ):
    import random
    ln = len(avlib)
    r = random.randrange(0,ln)
    return avlib[r]

def main():
    print('Welcome '+ name +' in tictac game ')
    boarddraw(board)
    print('------------------------')
    print('------------------------')

    while not(freespaceavliable(board)):
        if not(Winner(board,'O')):
            playermove()
            boarddraw(board)
            print('------------------------')
            print('------------------------')
        else:
            print('YOU LOST , Try again ')
            break

        if freespaceavliable(board):
            break

        if not(Winner(board,'X')):
            move=computermove()
            if move == 0:
                print(" ")
            else:

                insertlatter('O', move)
                boarddraw(board)
                print('------------------------')
                print('------------------------')

        else:
            print("You Won!")
            break

    if freespaceavliable(board):
              print("Match Tie")


name = (input("Enter you name : ").lower()).title()
print("Welcome "+ name + " in Tic Tac Game")
while True:
    x = input(name +" , You want to play then enter Y : ").lower()
    if x == 'y':
        board = [' ' for x in range(10)]
        print('----------------------------')
        main()
    else:
        break




