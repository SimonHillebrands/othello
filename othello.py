from PIL import Image 
import copy 

light_disk = Image.open("light_disk.png")
dark_disk = Image.open("dark_disk.png")
grey_disk = Image.open("grey_disk.png")

board = [[None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 0, 1, None, None, None],
        [None, None, None, 1, 0, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]]
def possibleMoves(disk):
    possible_board = copy.deepcopy(board)
    x = 0
    for rows in possible_board:
        y = 0
        for col in rows:
            if(col != disk and col != None and col!=2):
               # print(str(col)+"     "+str(disk))
                if(x>0):
                    if(possible_board[x-1][y] == None and x>0):
                        c = col 
                        i = 1
                        flag = False
                        while(c!=None and (i+x)<8):
                            c = possible_board[x+i][y]
                            if(c == disk):
                                flag = True
                            i+=1
                        if(flag):
                            possible_board[x-1][y] = 2
                    if(y>0):
                        if(possible_board[x-1][y-1] == None and x>0 and y>0):
                            c = col 
                            i = 1
                            flag = False
                            while(c!=None and (x+i)<8 and (y+i)<8):
                                c = possible_board[x+i][y+i]
                                if(c == disk):
                                    flag = True
                                i+=1
                            if(flag):
                                possible_board[x-1][y-1] = 2
                    if(y<7):
                        if(possible_board[x-1][y+1] == None and x>0 and y<7):
                            c = col 
                            i = 1
                            flag = False
                            while(c!=None and x+i<8 and y-i>-1):
                                c = possible_board[x+i][y-i]
                                if(c == disk):
                                    flag = True
                                i+=1
                            if(flag):
                                possible_board[x-1][y+1] = 2
                if(y>0):
                    if(possible_board[x][y-1] == None and y>0):
                        c = col 
                        i = 1
                        flag = False
                        while(c!=None and y+i<8):
                            c = possible_board[x][y+i]
                            if(c == disk):
                                flag = True
                            i+=1
                        if(flag):
                            possible_board[x][y-1] = 2
                if(x<7):
                    if(possible_board[x+1][y] == None and x<7):
                        c = col 
                        i = 1
                        flag = False
                        while(c!=None and x-i>-1):
                            c = possible_board[x-i][y]
                            if(c == disk):
                                flag = True
                            i+=1
                        if(flag):
                            possible_board[x+1][y] = 2
                    if(y<7):
                        if(possible_board[x+1][y+1] == None and x<7 and y<7):
                            c = col 
                            i = 1
                            flag = False
                            while(c!=None and x-i>-1 and y-i>-1):
                                c = possible_board[x-i][y-i]
                                if(c == disk):
                                    flag = True
                                i+=1
                            if(flag):
                                possible_board[x+1][y+1] = 2
                    if(y>0):
                        if(possible_board[x+1][y-1] == None and x<7 and y>0):
                            c = col 
                            i = 1
                            flag = False
                            while(c!=None and x-i>-1 and y+i<8):
                                c = possible_board[x-i][y+i]
                                if(c == disk):
                                    flag = True
                                i+=1
                            if(flag):
                                possible_board[x+1][y-1] = 2
                if(y<7):
                    if(possible_board[x][y+1] == None and y<7):
                        c = col 
                        i = 1
                        flag = False
                        while(c!=None and y-i>-1):
                            c = possible_board[x][y-i]
                            if(c == disk):
                                flag = True
                            i+=1
                        if(flag):
                            possible_board[x][y+1] = 2       
            y+=1    
        x+=1
    return possible_board
def updateBoardImage(turn):
    y = 0
    pboard = possibleMoves(turn)
    board_png = Image.open("board.png")
    for i in pboard:
        x = 0
        for j in i:
            #print(str(x)+ "  "+str(y))
            if(j == 0):
                board_png.paste(dark_disk,(x*102,y*102),dark_disk)
            if(j == 1):
                board_png.paste(light_disk,(x*102,y*102),light_disk)
            if(j == 2):
                board_png.paste(grey_disk,(x*102,y*102),grey_disk)
            x+=1
        x=0
        y+=1
    board_png.show()
def updateBoard(y,x,disk,board):
    if(x<7):
        if(board[x+1][y] != None and board[x+1][y] != disk):
            d = -1
            i = 1
            temp_board = copy.deepcopy(board)
            Flag = False
            while(d != disk and d!=None):
                d = temp_board[x+i][y]
                temp_board[x+i][y] = disk 
                if(d == disk and i>1):
                    Flag = True 
                i+=1
            if(Flag):
                board = copy.deepcopy(temp_board)
        if(y<7):
            if(board[x+1][y+1] != None and board[x+1][y+1] != disk):
                d = -1
                i = 1
                temp_board = copy.deepcopy(board)
                Flag = False
                while(d != disk and d!=None):
                    d = temp_board[x+i][y+i]
                    temp_board[x+i][y+i] = disk 
                    if(d == disk and i>1):
                        Flag = True 
                    i+=1
                if(Flag):
                   board = copy.deepcopy(temp_board)                    
        if(y>0):
            if(board[x+1][y-1] != None and board[x+1][y-1] != disk):
                d = -1
                i = 1
                temp_board = copy.deepcopy(board)
                Flag = False
                while(d != disk and d!=None):
                    d = temp_board[x+i][y-i]
                    temp_board[x+i][y-i] = disk 
                    if(d == disk and i>1):
                        Flag = True 
                    i+=1
                if(Flag):
                   board = copy.deepcopy(temp_board)                
    if(y<7):                
        if(board[x][y+1] != None and board[x][y+1] != disk):
            d = -1
            i = 1
            temp_board = board 
            temp_board = copy.deepcopy(board)
            Flag = False
            while(d != disk and d!=None):
                d = temp_board[x][y+i]
                temp_board[x][y+i] = disk 
                if(d == disk and i>1):
                    Flag = True 
                i+=1
            if(Flag):
               board = copy.deepcopy(temp_board)                
    if(y>0):
        if(board[x][y-1] != None and board[x][y-1]!= disk):
            d = -1
            i = 1
            temp_board = copy.deepcopy(board)
            Flag = False
            while(d != disk and d!=None):
                d = temp_board[x][y-i]
                temp_board[x][y-i] = disk 
                if(d == disk and i>1):
                    Flag = True 
                i+=1
            if(Flag):
                board = copy.deepcopy(temp_board)
    if(x>0):
        if(board[x-1][y] != None and board[x-1][y] != disk):
            d = -1
            i = 1
            temp_board = copy.deepcopy(board)
            Flag = False
            while(d != disk and d!=None):
                d = temp_board[x-i][y]
                temp_board[x-i][y] = disk 
                if(d == disk and i>1):
                    Flag = True 
                i+=1
            if(Flag):
                board = copy.deepcopy(temp_board)
        if(y>0):
            if(board[x-1][y-1] != None and board[x-1][y-1]!= disk):
                d = -1
                i = 1
                temp_board = copy.deepcopy(board)
                Flag = False
                while(d != disk and d!=None):
                    d = temp_board[x-i][y-i]
                    temp_board[x-i][y-i] = disk 
                    if(d == disk and i>1):
                        Flag = True 
                    i+=1
                if(Flag):
                    board = copy.deepcopy(temp_board)
        if(y<7):
            if(board[x-1][y+1] != None and board[x-1][y+1] != disk):
                d = -1
                i = 1
                temp_board = copy.deepcopy(board)
                Flag = False
                while(d != disk and d!=None):
                    d = temp_board[x-i][y+i]
                    temp_board[x-i][y+i] = disk 
                    if(d == disk and i>1):
                        Flag = True 
                    i+=1
                if(Flag):
                    board = copy.deepcopy(temp_board)    
    return(board)            
updateBoardImage(0)
game = True
turn = -1
while(game):
    if(turn == -1):
        possible_board = possibleMoves(0)
       # if(2 not in possible_board):
          #  game = False 
        valid = True
        while(valid):
            move = input()
            x = int(move[0])
            y = int(move[1])
            if(possible_board[x][y] == 2):
                board[y][x] = 0
                board = updateBoard(x,y,0,board)
                valid = False 
            if(valid):
                print("Not a legal move")
        updateBoardImage(1)
    else:
        possible_board = possibleMoves(1)
      #  if(2 not in possible_board):
           # game = False 
        valid = True
        while(valid):
            move = input()
            x = int(move[0])
            y = int(move[1])
            if(possible_board[y][x] == 2):
                board[y][x] = 1
                board = updateBoard(x,y,1,board)
                valid = False 
            if(valid):
                print("Not a legal move")
        updateBoardImage(0)
    turn*=-1
print("GAME OVER")