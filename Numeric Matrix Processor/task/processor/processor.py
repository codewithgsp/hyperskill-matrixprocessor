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

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix(matrix=[[self.matrix[r][c] * other for c in range(self.__c)] for r in range(self.__r)])
        if self.__check_dimension_mul(other.matrix):
            return self.__matrix_multiplication(other)
        else:
            return self.error_msg

    def __matrix_multiplication(self, other):
        return Matrix(matrix=[[sum(a * b for a, b in zip(row_x, col_y)) for col_y in zip(*other.matrix)] for row_x in self.matrix])

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


class Processor:
    options = ['Add matrices', 'Multiply matrix by a constant', 'Multiply matrices']

    def play(self):
        while True:
            self.display_options()
            user_input = input()
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

    def display_options(self):
        for i, option in enumerate(self.options, start=1):
            print(f'{i}. {option}')
        print('0. Exit')


processor = Processor()
processor.play()
