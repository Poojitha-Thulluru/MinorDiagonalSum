def minor_diagonal_sum(input_matrix: list, n_rows: int, n_columns: int):
    minor_diagonal_sum: int = 0
    for row in range(n_rows):
        n_columns -= 1
        minor_diagonal_sum += input_matrix[row][n_columns]
    return minor_diagonal_sum


try:
    rows = int(input("Enter number of rows : "))
    columns = int(input("Enter number of columns : "))
    matrix = [[int(input(f"Enter element ({x},{y}) to insert into matrix : ")) for x in range(columns)]
              for y in range(rows)]
    print("The Main Diagonal Sum of the given matrix is : ", minor_diagonal_sum(matrix, rows, columns))
except ValueError:
    print("Invalid Input. Please enter only integers")
