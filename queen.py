def solve_n_queens(n):
    def is_safe(board, row, col):
        
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            
            if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def backtrack(row):
        if row == n:
            
            solutions.append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()


solutions = solve_n_queens(4)
print_solutions(solutions)
