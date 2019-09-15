#In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

def toeplitz(matrix):
    validate = []
    for i in range(len(matrix)):
        validate.append(matrix[i][i:])
    print(validate)
    end = len(validate)-1
    final_length = len(validate[end])
    while end>0:
        if validate[end] != validate[end-1][:final_length]:
            print('false')
            return False
        end-=1
        final_length+=1
    print('true')
    return True





test = [[1, 2, 3 ,4, 8],
[5, 1, 2, 3, 4],
[4, 5, 1, 2, 3],
[7,4, 5, 1, 2]]

toeplitz(test)