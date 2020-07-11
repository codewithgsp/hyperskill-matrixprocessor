from copy import copy


class Matrix:

    error_msg = 'The operation cannot be performed.'

    def __init__(self,  number=None, matrix=None):
        self.number = number
        self.matrix = matrix
        if self.matrix is None:
            self.__create_from_input()

    def __str__(self):
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.matrix)

    def __add__(self, other):
        if self.__check_dimension_add(other.matrix):
            return Matrix(matrix=[[self.matrix[r][c] + other.matrix[r][c]
                                   for c in range(self.__c)] for r in range(self.__r)])
        else:
            return self.error_msg

    def __len__(self):
        return len(self.matrix)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix(matrix=[[self.matrix[r][c] * other for c in range(self.__c)] for r in range(self.__r)])
        if self.__check_dimension_mul(other.matrix):
            return self.__matrix_multiplication(other)
        else:
            return self.error_msg

    def __matrix_multiplication(self, other):
        return Matrix(matrix=[[sum(a * b for a, b in zip(row_x, col_y)) for col_y in zip(*other.matrix)]
                              for row_x in self.matrix])

    def __create_from_input(self):
        self.__r, self.__c = map(int, input('Enter size of {} matrix:'.format(self.number)).split(' '))
        print('Enter {} matrix:'.format(self.number))
        self.matrix = []
        for _ in range(self.__r):
            converted_row_matrix = []
            for element in input().split(' '):
                if '.' in element:
                    converted_row_matrix.append(float(element))
                else:
                    converted_row_matrix.append(int(element))
            self.matrix.append(converted_row_matrix)

    def __check_dimension_add(self, matrix):
        return True if len(self.matrix) == len(matrix) and len(self.matrix[0]) == len(matrix[0]) else False

    def __check_dimension_mul(self, matrix):
        return True if len(self.matrix[0]) == len(matrix) else False

    def __check_square_matrix(self):
        return True if len(self.matrix) == len(self.matrix[0]) else False

    @staticmethod
    def get_matrix_minor(m, i, j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    @staticmethod
    def get_cofactor_matrix(m):

        #  special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1], -1 * m[0][1]], [-1 * m[1][0], m[0][0]]]

        #  find matrix of co_factors
        co_factors = []
        for r in range(len(m)):
            cofactor_row = []
            for c in range(len(m)):
                minor = Matrix.get_matrix_minor(m, r, c)
                cofactor_row.append(((-1)**(r+c)) * Matrix.get_determinant(minor))
            co_factors.append(cofactor_row)
        return Matrix(matrix=co_factors)

    @staticmethod
    def get_determinant(matrix, total=0):

        # store indices in list for row ref
        indices = list(range(len(matrix)))

        # base ends
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0]

        if len(matrix) == 2 and len(matrix[0]) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

        # focused columns
        for fc in indices:
            _as = copy(matrix)  # copy the matrix
            _as = _as[1:]
            height = len(_as)

            for i in range(height):
                _as[i] = _as[i][0:fc] + _as[i][fc+1:]

            sign = (-1) ** (fc % 2)
            sub_det = Matrix.get_determinant(_as)
            total += sign * matrix[0][fc] * sub_det
        return total

    def transpose(self, option):
        transposed_matrix = [['*' for _ in range(self.__r)] for _ in range(self.__c)]
        if option == '1':
            for i in range(self.__r):
                for j in range(self.__c):
                    if transposed_matrix[j][i] == '*':
                        transposed_matrix[j][i] = self.matrix[i][j]
            return Matrix(matrix=transposed_matrix)
        if option == '2':
            column = self.__c
            for i in range(self.__c):
                row = self.__r
                column += -1
                for j in range(self.__r):
                    row += -1
                    if transposed_matrix[i][j] == '*':
                        transposed_matrix[i][j] = self.matrix[row][column]
            return Matrix(matrix=transposed_matrix)
        if option == '3':
            for i in range(self.__c):
                column = self.__c
                for j in range(self.__r):
                    column += -1
                    if transposed_matrix[i][j] == '*':
                        transposed_matrix[i][j] = self.matrix[i][column]
            return Matrix(matrix=transposed_matrix)
        if option == '4':
            row = self.__r
            for i in range(self.__c):
                row += -1
                for j in range(self.__r):
                    if transposed_matrix[i][j] == '*':
                        transposed_matrix[i][j] = self.matrix[row][j]
            return Matrix(matrix=transposed_matrix)


class Processor:
    options = ['Add matrices',
               'Multiply matrix by a constant',
               'Multiply matrices',
               'Transpose matrix',
               'Calculate a determinant',
               'Inverse matrix']

    transpose_options = ['Main diagonal',
                         'Side diagonal',
                         'Vertical line',
                         'Horizontal line']

    def play(self):
        while True:
            self.display_options(self.options)
            print('0. Exit')
            user_input = input('Your choice:')
            if user_input == '0':
                exit(0)
            if user_input == '1':
                result = Matrix(number='first') + Matrix(number='second')
                print(f'The result is:\n{result}\n')
            elif user_input == '2':
                m1 = Matrix()
                constant = float(input('Enter constant:'))
                result = m1 * constant
                print(f'The result is:\n{result}\n')
            elif user_input == '3':
                result = Matrix(number='first') * Matrix(number='second')
                print(f'The result is:\n{result}\n')
            elif user_input == '4':
                self.display_options(self.transpose_options)
                user_requested_transpose = input('Your choice:')
                if user_requested_transpose in ('1', '2', '3', '4'):
                    m1 = Matrix(number='')
                    print('option', user_requested_transpose)
                    result = m1.transpose(user_requested_transpose)
                    print(f'The result is:\n{result}\n')
            elif user_input == '5':
                m1 = Matrix(number='')
                result = Matrix.get_determinant(m1.matrix)
                print(f'{result}\n')
            elif user_input == '6':
                m1 = Matrix(number='')
                determinant = Matrix.get_determinant(m1.matrix)
                if determinant == 0:
                    print("This matrix doesn't have an inverse.\n")
                else:
                    cofactor_matrix = Matrix.get_cofactor_matrix(m1.matrix)
                    length = len(cofactor_matrix.matrix)
                    transposed_matrix = [['*' for _ in range(length)] for _ in range(length)]
                    for i in range(length):
                        for j in range(length):
                            if transposed_matrix[j][i] == '*':
                                transposed_matrix[j][i] = cofactor_matrix.matrix[i][j]
                    result = [[transposed_matrix[r][c] * (1 / determinant) for c in range(length)] for r in range(length)]
                    for row in result:
                        print(" ".join(str(cell) for cell in row))

    def display_options(self, options):
        for i, option in enumerate(options, start=1):
            print(f'{i}. {option}')


processor = Processor()
processor.play()
