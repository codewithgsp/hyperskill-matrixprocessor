class NumericMatrixProcessor:

    def __init__(self, row, column, matrix):
        self.row = row
        self.column = column
        self.matrix = matrix

    def add_matrix(self, matrix):
        result_matrix = []
        for row in range(0, self.row):
            row_matrix = []
            for column in range(0, self.column):
                row_matrix.append(str(self.matrix[row][column] + matrix[row][column]))
            result_matrix.append(row_matrix)
        return result_matrix


matrix_object_dict = {}
for k in range(1, 3):
    u_row, u_column = list(map(int, input().split(' ')))
    u_matrix = []
    for _ in range(u_row):
        u_row_matrix = list(map(int, input().split(' ')))
        u_matrix.append(u_row_matrix)
    matrix_object_dict[f'matrix_{k}'] = NumericMatrixProcessor(u_row, u_column, u_matrix)

if (matrix_object_dict['matrix_1'].row == matrix_object_dict['matrix_2'].row
        and matrix_object_dict['matrix_1'].column == matrix_object_dict['matrix_2'].column):
    result = matrix_object_dict['matrix_1'].add_matrix(matrix_object_dict['matrix_2'].matrix)
    for i in range(matrix_object_dict['matrix_1'].row):
        print(" ".join(result[i]))
else:
    print('ERROR')
