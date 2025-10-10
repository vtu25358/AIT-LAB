# Python3 program to solve N Queen Problem using backtracking

# Global variable for board size
N = 4

# Function to print the board
def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Function to check if a queen can be placed on board[row][col]
def isSafe(board, row, col):

    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Recursive utility function to solve N Queen problem
def solveNQUtil(board, col):
    # Base case: If all queens are placed
    if col >= N:
        return True

    # Try placing queen in each row for this column
    for i in range(N):
        if isSafe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1):
                return True

            # If placing queen doesn't lead to a solution, backtrack
            board[i][col] = 0

    return False

# Function to solve N Queen problem
def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

# Driver Code
if __name__ == '__main__':
    solveNQ()
