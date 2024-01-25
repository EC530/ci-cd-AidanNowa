def matrix_mult(matrix1, matrix2):
    pass



def test_answer():
    assert matrix_mult( [[12,7,3], [4 ,5,6], [7 ,8,9]], [[5,8,1], [6,7,3], [4,5,9]]) == [[114, 160, 60], [74, 97, 73], [119, 157, 112]] 
    assert matrix_mult( [[0,0], [1,1]], [[1,1], [0,0]]) == [[0,0], [1,1]]
    assert matrix_mult( [[1,1], [1,1]], [[0,0], [0,0]]) == [[0,0], [0,0]]
    assert matrix_mult( [[1,2,3], [4,5,6], [7,8,9]], [[1,2],[3,4],[5,6]]) ==  [[22,28],[49,64],[76,100]]
    assert matrix_mult( [[1,2,3]], [[1],[2],[3]]) == 14
    assert matrix_mult( [[1,1,1], [2,2,2], [3,3,3]], [[1,1],[2,2]]) == "Error" # Incorrect matrix dimensions TODO: how to implmement error testing in pytest
    assert matrix_mult( [[]], [[1,2],[3,4]]) == "Error" #empty matrix
    # R: matrix by a scalar
    # R: characters & numbers
    # check for outofbounds inputs (max values)
    # check for correct user inputs -- test input validation