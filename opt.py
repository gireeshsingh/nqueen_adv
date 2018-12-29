#10 queen
#0 open
#1 block
#3 cant place since queen will attack
import time

def nqueens():
    rows=int(input("Enter the number of rows:"))
    cols=int(input("Enter the number of cols:"))
    i=0
    arr=[]
    while(i<rows):
        arr.append(input())
        i=i+1
    i=0
    print("Input Accepted")
    t1=time.time()
    queensBoard(arr)
    t2=time.time()
    print("Time Taken:",(t2-t1))
    
def queensBoard(arr):
    #t1=time.time()
    rows=len(arr)
    cols=len(arr[0])
    newboard=[]
    i=0
    j=0
    while(i<rows):
        j=0
        okko=[]
        while(j<cols):
            if(arr[i][j]=="."):
                okko.append(0)#open_square
            elif(arr[i][j]=="#"):
                okko.append(1)#blocked_square
            j=j+1
        newboard.append(okko)
        i=i+1
    max_queens=available_positions(newboard,0,0,rows,cols)
    solution=[[0]]
    i=0
    j=0
    while(i<rows):
        while(j<cols):
            if(newboard[i][j]!=1):
                newboard[i][j]=10
                solution.append(updateboard([row[:] for row in newboard],i,j,rows,cols))
                newboard[i][j]=0
            j=j+1
        i=i+1
        j=0
    solution.pop(0)
    i=0
    index=0
    all_solutions=[row[:] for row in solution]
    final_solution=queensBoardss(solution,rows,cols,all_solutions)
    #t2=time.time()
    answer=len(all_solutions)
    print(answer)
    #print("Time Taken:",(t2-t1))

def available_positions(board,k,l,rows,cols):
    i=k
    j=l
    avail=0
    while(i<rows):
        while(j<cols):
            if(board[i][j]==0):
                avail=avail+1
            j=j+1
        i=i+1
        j=0
    return avail

def updateboard(oldboard,i,j,rows,cols):
    board=[row[:] for row in oldboard]
    r=i+1
    c=j
    while(r<rows):
        if(board[r][c]==1):#if blocked then stop updating
            break
        if(board[r][c]==0):#if open then update
            board[r][c]=3
        r=r+1
    r=i
    c=j+1
    while(c<cols):
        if(board[r][c]==1):#if blocked then stop updating
            break
        if(board[r][c]==0):#if open then update
            board[r][c]=3
        c=c+1
    r=i-1
    c=j
    while(r>=0):
        if(board[r][c]==1):#if blocked then stop updating
            break
        if(board[r][c]==0):#if open then update
            board[r][c]=3
        r=r-1
    r=i
    c=j-1
    while(c>=0):
        if(board[r][c]==1):#if blocked then stop updating
            break
        if(board[r][c]==0):#if open then update
            board[r][c]=3
        c=c-1
    r=i+1
    c=j+1
    while(c<cols and r<rows):
        if(board[r][c]==1):#if blocked then stop updating
            break
        if(board[r][c]==0):#if open then update
            board[r][c]=3
        c=c+1
        r=r+1
    r=i-1
    c=j-1
    while(c>=0 and r>=0):
        if(board[r][c]==1):#if blocked then stop updating
            break
        if(board[r][c]==0):#if open then update
            board[r][c]=3
        c=c-1
        r=r-1
    r=i+1
    c=j-1
    while(c>=0 and r<rows):
        if(board[r][c]==1):#if blocked then stop updating
            break
        if(board[r][c]==0):#if open then update
            board[r][c]=3
        c=c-1
        r=r+1
    r=i-1
    c=j+1
    while(c<cols and r>=0):
        if(board[r][c]==1):#if blocked then stop updating
            break
        if(board[r][c]==0):#if open then update
            board[r][c]=3
        c=c+1
        r=r-1
    return board
    
def queensBoardss(tempsolution,rows,cols,all_solutions):
    solution=[row[:] for row in tempsolution]
    i=0
    j=0
    k=0
    while(i<len(solution)):
       # print("LOG")
        #board=solution[i]
        j=0
        popflag=0
        refboard=[row[:] for row in solution[i]]
        while(j<rows):
            while(k<cols):
                if(refboard[j][k]==0):
                    nnboard=[row[:] for row in refboard]
                    nnboard[j][k]=10#place_queen
                    tempboard=updateboard(nnboard,j,k,rows,cols)                    
                    if(tempboard not in all_solutions):
                        solution[i].append(tempboard)
                        all_solutions.append(tempboard)
                        if(popflag==0):
                            pl=0
                            while(pl<rows):
                                solution[i].pop(0)
                                pl=pl+1
                            popflag=1
                        #board=[row[:] for row in refboard]
                k=k+1
            j=j+1
            k=0
        if(isinstance(solution[i][0][0],list)):
            if(isinstance(solution[i][0][0][0],int)):
                ktemp=queensBoardss(solution[i],rows,cols,all_solutions)
                solution[i]=[row[:] for row in ktemp]
        i=i+1
    return solution

nqueens()