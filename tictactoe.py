# Tic Tac Toe

 

board = [
 ["-","-","-"],
 ["-","-","-"],
 ["-","-","-"]
 
 ]


user  = True 
turns = 0
def print_board(board):
    for i in board:
        for j in i:
            print(f"{j} ", end = " ")
        print()
         

def quit(userinput):
    if(userinput.lower() == "q"):
        return True
    else: return False
def checkinput(userinput):
    if not isnum(userinput): return False
    userinput = int(userinput)

    if not fitrange(userinput): return False

    return True

    

def isnum(userinput):
    if userinput.isnumeric()== False:
        print("This is not a valid number")
        return False
    else: 
        
        return True
def fitrange(userinput):
    if userinput >9 or userinput <1:
       print("This number is out of bounds")
       return False
    else: return True

def taken(coords, board):
    row = coords[0]   
    col = coords[1]
    if board[row][col] != "-":
        print("Position is already taken")
        return True
    return False
  

def coordinates(userinput):
    row = int(userinput/3)
    col = userinput
    if col >2: 
        col = int(col%3)
    return(row, col)

def add(coords, board, activeuser):
    board[coords[0]][coords[1]] = activeuser

def currentuser(user):
    if user == True:
        return "x"
    else:
        return "o"
def haswon(user, board):
    if checkrow(user, board):
        return True
    if checkcolumn(user, board):
        return True
    if checkdiagonal(user, board):
        return True
def checkrow(user,board):
    for i in board:
        completerow= True
        for j in i:
            if j!= user:
                completerow = False
                break
        if completerow: 
            return True
    return False
def checkcolumn(user, board):
    
    for i in range(len(board)):
        completecolumn =  True
        for j in range(len(board)):
            if board[j][i] != user:
                completecolumn= False
                break
        if completecolumn:
            return True
    return False
def checkdiagonal(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board [1][1] == user and board[2][0] == user:
        return True
    else:
        return False

while turns <9:
    activeuser = currentuser(user)
    print_board(board)

    userinput = input("Please enter a number between 1 and 9 or enter \"q\" to quit: ")
    if quit(userinput) == True:
        print("You have quit, Thanks for playing")
        break

    if checkinput(userinput) == False:
        print("Please try again.")
        continue
    userinput = int(userinput) -1
    coords = coordinates(userinput)

    if taken(coords, board):
        print("Please try again")
        continue
    add(coords,board, activeuser)

    if haswon(activeuser, board):
        print_board(board)
        print(f"{activeuser.upper()}  has won!")
        break
    turns +=1
    if turns == 9:
        print("It's a tie!")
    user = not user