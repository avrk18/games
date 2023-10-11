# Code to Measure time taken by program to execute
import time
# store starting time
begin = time.time()
player, opponent = 'x', 'o'


# This function is to check end game 1, if all cells are used
# If there are moves left returns true
# Else returns False
def MovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                return True
    return False


# This function is where the minimax algorithm kicks in
# Assigning a value +10 to end cases where Computer wins
# Asssigning a value -10 to end case where Opponent wins
# Value of 0 to all other intermediate games and end game 1.

def evaluate(b):
    # Checking for Rows for X or O victory and assignment of respective value.
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == player):
                return 10
            elif (b[row][0] == opponent):
                return -15

    # Checking for Columns for X or O victory and assignment of respective value.
    for col in range(3):

        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

            if (b[0][col] == player):
                return 10
            elif (b[0][col] == opponent):
                return -15

    # Checking for Diagonals for X or O victory and assignment of respective value.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

        if (b[0][0] == player):
            return 10
        elif (b[0][0] == opponent):
            return -15

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

        if (b[0][2] == player):
            return 10
        elif (b[0][2] == opponent):
            return -15

    # Else if none of them have won then return 0
    return 0


# This is the minimax function.
# Parameters taken in are board - to access the current board state,
# depth - for iterative depth search , isMax - to check for turn
# First checks for endgame possibilities
# Now we iteratively go through till each case reaches end game(nodes)\
# We then backtrack assigning max value of node(n+1) if it is computer's turn
# min value of node(n+1) if it is opponents move
# We do so until depth has returned to 0 determine value of each move
# In this model alpha-beta pruning is added to help remove redundant cases
# Suppose a minimiser already has a path with maximum utility 10 and the
# next path has an element of utility 20, the rest of the paths don't need
# to be checked and are redundant hence pruned. Similarly for a maximiser.
def minimax(board, depth, isMax, alpha, beta):
    score = evaluate(board)

    # Returning 10 if computer has won and game_over
    if (score == 10):
        return score

    # Returning -10 if computer has lost and game_over
    if (score == -15):
        return score

    # If there are no more moves and no winner then
    # it is a tie
    if (MovesLeft(board) == False):
        return 0

    # If it is computers move
    if (isMax):
        best = -1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if (board[i][j] == '_'):
                    # Make the move
                    board[i][j] = player

                    # Call minimax recursively and choose
                    # the maximum value
                    best = max(best, minimax(board,
                                             depth + 1,
                                             not isMax, alpha, beta))
                    alpha = max(alpha, best)
                    board[i][j] = '_'

                    #pruning is done here for maximiser
                    if beta <= alpha:
                        break

        return best

    # If opponents move
    else:
        best = 1000

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if (board[i][j] == '_'):
                    # Make the move
                    board[i][j] = opponent

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, depth + 1, not isMax, alpha, beta))

                    beta = min(beta, best)
                    board[i][j] = '_'

                    #pruning is done here for minimiser
                    if beta <= alpha:
                        break
        return best

    # This will return the best possible move for the player


def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    # Generating minmax value for all empty cells
    # Returning position with max value
    for i in range(3):
        for j in range(3):

            # Check if cell is empty
            if (board[i][j] == '_'):

                # Make the move
                board[i][j] = player

                # compute evaluation function for this
                # move.
                moveVal = minimax(board, 0, False, 0,1000)

                # Undo the move
                board[i][j] = '_'

                # If the value of the current move is
                # more than the best value, then update
                # best/
                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    print("The value of the best Move is :", bestVal)
    print()
    return bestMove


# Driver code
board = [
    ['o', '_', 'x'],
    ['_', 'x', '_'],
    ['_', '_', 'o']
]

bestMove = findBestMove(board)

print("The Optimal Move is :")
print("ROW:", bestMove[0], " COL:", bestMove[1])
# store end time
end = time.time()
# total time taken
print(f"Total runtime of the program is {end - begin}")