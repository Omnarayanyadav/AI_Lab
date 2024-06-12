#nQueens problem
def display(board):
    for row in board:
        print(row)
        
def isSafe(board, x, y, n):
    #column test
    for row in range(x):
        if(board[row][y] == 'Q'):
            return False
        
    #Top-left  Diagonal test
    row = x - 1
    col = y - 1
    while row>=0 and col>=0:
        if(board[row][col] == 'Q'):
            return False
        
        row -= 1
        col -= 1
    
    
        
    #Top-right Diagonal test
    row = x - 1
    col = y + 1
    while row>=0 and col<n:
        if(board[row][col] == 'Q'):
            return False
        row -= 1
        col += 1
    return True

def nQueenSolver(board, x, n):
        #if nQueens are placed returns true
        if(x>=n):
            return True
        #iterate through columns for each row
        for col in range(n):
            #if the pos is safe then place queen
            if(isSafe(board, x, col, n)):
                board[x][col] = 'Q'
            #if the next queen can be placed retuern True
                if(nQueenSolver(board, x+1, n)):
                    return True
            #else backtrack
            
                board[x][col] = ' '
        return False
    
n = int(input("Enetr n: ")) 
board = [[' ']*n for i in range(n)]     

if(nQueenSolver(board,0,n)):
    display(board)
else:
    print("No solution!!!!")