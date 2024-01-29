def is_numeric_matrix(matrix):
    """Check if the matrix contains only numeric values."""
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            return False
    return True

def can_multiply_matrices(A, B):
    """Check if two matrices A and B can be multiplied."""
    if not A or not B or not A[0] or not B[0]:
        return False, "One of the matrices is empty."
    if len(A[0]) != len(B):
        return False, "Incompatible matrix sizes for multiplication."
    if not is_numeric_matrix(A) or not is_numeric_matrix(B):
        return False, "Matrices must contain only numbers."
    return True, ""

def matrix_multiply(A, B):
    """Multiply two matrices A and B."""
    valid, message = can_multiply_matrices(A, B)
    if not valid:
        return message

    if A == 1:
        return "Special case found"

    result = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result

