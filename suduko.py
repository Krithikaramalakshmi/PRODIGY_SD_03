def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
def find_empty_location(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
    return None
def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True
def solve_sudoku(grid):
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True  # Puzzle solved
    row, col = empty_location
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Undo the move
    return False
def get_user_input():
    """Prompt the user to enter the Sudoku grid."""
    print("Enter the Sudoku puzzle row by row, using 0 for empty cells.")
    grid = []
    for i in range(9):
        while True:
            try:
                row = input(f"Enter row {i+1} (9 numbers separated by spaces): ")
                row_list = [int(num) for num in row.split()]
                if len(row_list) == 9:
                    grid.append(row_list)
                    break
                else:
                    print("Please enter exactly 9 numbers.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    return grid
if __name__ == "__main__":
    sudoku_grid = get_user_input()
    print("Solving the Sudoku puzzle...")
    if solve_sudoku(sudoku_grid):
        print("Sudoku puzzle solved:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists for the given Sudoku puzzle.")
