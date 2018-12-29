import pprint
import copy
import time

accepted_solutions=[[[0,0,0],[0,0,0],[0,0,0]]]

def nqueens():
    rows=int(input("Enter the number of rows:"))
    cols=int(input("Enter the number of cols:"))
    i=0
    j=0
    arr=[]
    newboard=[]
    while(i<rows):
        arr.append(input())
        i=i+1
    i=0
    print("Input Accepted")
    t1=time.time()
    while(i<rows):
        j=0
        okko=[]
        while(j<cols):
            okko.append(arr[i][j])
            j=j+1
        newboard.append(okko)
        i=i+1
    queensBoard(newboard,rows,cols)
    t2=time.time()
    print("Time Taken:",t2-t1)
    
    
def queensBoard(board,rows,cols):
    print(board)
    #rows=len(board)
    #cols=len(board[0])
    i=0
    j=0
    total=available_positions(board,i,j,rows,cols)+possible_combination(board,rows,cols)    
    print(total)

def possible_combination(board,rows,cols):
    total=0
    i=0
    j=0
    k=0
    tempboard=[row[:] for row in board]
    no_of_queens=2
    #loopcount=0
    breakvalue=0
    max_queens=available_positions(board,i,j,rows,cols)
    while(no_of_queens<max_queens):
        i=0
        breakvalue=0
        while(i<rows):
            if(breakvalue==1):
                break
            j=0
            while(j<cols):
                number_of_available_positions=available_positions(board,i,j,rows,cols)
                if(number_of_available_positions>=no_of_queens):
                    if(board[i][j]=="#"):
                        k=0
                    else:
                        k=0
                        ok=available_positions(board,i,j,rows,cols)
                        if(ok<7):
                            ok=7
                        while(k<ok):
                            k=k+1
                            board=[row[:] for row in tempboard]
                            total=total+recursive_func(accepted_solutions,board,no_of_queens,0,rows,cols,i,j,0)
                            #loopcount=loopcount+1
                else:
                    breakvalue=1
                    break
                j=j+1
            i=i+1
        no_of_queens=no_of_queens+1
    return total

def available_positions(board,k,l,rows,cols):
    i=k
    j=l
    avail=0
    # for i in range(rows):
        # avail=avail+board[i].count(".")
    # return avail
    # while(i<rows):
        # avail=avail+board[i].count(".")
        # i=i+1
    # return avail
    while(i<rows):
        while(j<cols):
            if(board[i][j]=="."):
                avail=avail+1
            j=j+1
        i=i+1
        j=0
    return avail

#def recursive_func(accepted_solutions,tempboard,no_of_queens,queens_placed,rows,cols,start_row,start_col,total):
def recursive_func(accepted_solutions,tempboard,no_of_queens,queens_placed,rows,cols,i,j,total):
    if(queens_placed==no_of_queens and (tempboard not in accepted_solutions)):#check_if_new_solution(accepted_solutions,tempboard)):
        total=total+1
        accepted_solutions.append([row[:] for row in tempboard])
        return total
    # i=start_row
    # j=start_col
    while(i<rows):
        while(j<cols):
            if(valid_placement(accepted_solutions,tempboard,rows,cols,i,j)):# and check_if_new_solution(accepted_solutions,tempboard)):
                queens_placed=queens_placed+1
                swap=tempboard[i][j]
                tempboard[i][j]=1
                if((j+1)>=cols):
                    total=recursive_func(accepted_solutions,tempboard,no_of_queens,queens_placed,rows,cols,i+1,0,total)
                else:
                    total=recursive_func(accepted_solutions,tempboard,no_of_queens,queens_placed,rows,cols,i,j+1,total)
                queens_placed=queens_placed-1
                tempboard[i][j]=swap
            j=j+1
        i=i+1
        j=0
    
    return total
                
# def check_if_new_solution(accepted_solutions,board):
    # if(board in accepted_solutions):
        # return False
    # return True

def valid_placement(accepted_solutions,board,rows,cols,row,col):
    if(board[row][col]=="#"):
        return False
    i=0
    j=0
    while((col-j)>=0):
        if(board[row][col-j]==1):# and is_unblocked_route(board,row,col,row,j)):
            return False
        if(board[row][col-j]=="#"):
            break
        j=j+1
    i=0
    j=0
    while((col+j)<cols):
        if(board[row][col+j]==1):# and is_unblocked_route(board,row,col,row,j)):
            return False
        if(board[row][col+j]=="#"):
            break
        j=j+1
    i=0
    j=0
    while((row-i)>=0):
        if(board[row-i][col]==1):# and is_unblocked_route(board,row,col,i,col)):
            return False
        if(board[row-i][col]=="#"):
            break
        i=i+1
    i=0
    j=0
    while((row+i)<rows):
        if(board[row+i][col]==1):# and is_unblocked_route(board,row,col,i,col)):
            return False
        if(board[row+i][col]=="#"):
            break
        i=i+1
    i=0
    j=0
    while(i<rows and i<cols):
        if((row-i)>=0 and (col-i)>=0 and board[row-i][col-i]==1):#is_unblocked_route(board,row,col,row-i,col-i)):
            return False
        if((row-i)>=0 and (col-i)>=0 and board[row-i][col-i]=="#"):
            break
        i=i+1
    
    i=0
    j=0
    while(i<rows and i<cols):
        if((row+i)<rows and (col+i)<cols and board[row+i][col+i]==1):# and is_unblocked_route(board,row,col,row+i,col+i)):
            return False
        if((row+i)<rows and (col+i)<cols and board[row+i][col+i]=="#"):
            break
        i=i+1
        
    i=0
    j=0
    while(i<rows and i<cols):
        if((row+i)<rows and (col-i)>=0 and board[row+i][col-i]==1):# and is_unblocked_route(board,row,col,row+i,col-i)):
            return False
        if((row+i)<rows and (col-i)>=0 and board[row+i][col-i]=="#"):
            break
        i=i+1
        
    i=0
    j=0
    while(i<rows and i<cols):
        if((row-i)>=0 and (col+i)<cols and board[row-i][col+i]==1):# is_unblocked_route(board,row,col,row-i,col+i)):
            return False
        if((row-i)>=0 and (col+i)<cols and board[row-i][col+i]=="#"):
            break
        i=i+1
        
    return True
    
nqueens()










