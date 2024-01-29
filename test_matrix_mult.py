import pytest

from matrix_mult import matrix_multiply

@pytest.mark.parametrize("matrix_a, matrix_b, expected", [
    ([[12,7,3], [4 ,5,6], [7 ,8,9]], [[5,8,1], [6,7,3], [4,5,9]], [[114, 160, 60], [74, 97, 73], [119, 157, 112]]),
    ([[0,0], [1,1]], [[1,1], [0,0]], [[0,0], [1,1]]),
    ([[1,1], [1,1]], [[0,0], [0,0]], [[0,0], [0,0]]),
    ([[1,2,3], [4,5,6], [7,8,9]], [[1,2],[3,4],[5,6]], [[22,28],[49,64],[76,100]]),
    ([[1,2,3]], [[1],[2],[3]], 14),
    ([[1,1,1], [2,2,2], [3,3,3]], [[1,1],[2,2]], "Incompatible matrix sizes for multiplication."),  # Incorrect matrix dimensions
    ([[]], [[1,2],[3,4]], "One of the matrices is empty."),  # Empty matrix
])
def test_matrix_mult(matrix_a, matrix_b, expected):
    assert matrix_multiply(matrix_a, matrix_b) == expected