import matrix_mult

def main():
    print("Enter the first matrix, row by row. Type 'done' to finish:")
    matrix1 = []
    while True:
        row = input()
        if row.strip().lower() == 'done':
            break
        matrix1.append([float(num) for num in row.split()])

    print("Enter the second matrix, row by row. Type 'done' to finish:")
    matrix2 = []
    while True:
        row = input()
        if row.strip().lower() == 'done':
            break
        matrix2.append([float(num) for num in row.split()])

    result = matrix_mult.matrix_multiply(matrix1, matrix2)
    if isinstance(result, str):
        print(f"Error: {result}")
    else:
        print("Resultant Matrix:")
        for row in result:
            print(row)

if __name__ == "__main__":
    main()
