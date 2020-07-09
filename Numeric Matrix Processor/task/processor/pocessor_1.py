from time import time


class Matrix:

    def __init__(self, matrix=None):
        self.matrix = matrix
        if self.matrix is None:
            self.__create_from_input()

    def __str__(self):
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.matrix)

    def __add__(self, other):
        if self.__check_dimension(other.matrix):
            return Matrix([[self.matrix[n][m] + other.matrix[n][m] for m in range(self.__m)] for n in range(self.__n)])
        else:
            return 'ERROR'

    def __create_from_input(self):
        self.__n, self.__m = map(int, input().split(' '))
        self.matrix = [list(map(int, input().split(' '))) for i in range(self.__n)]

    def __check_dimension(self, matrix):
        return True if len(self.matrix) == len(matrix) and len(self.matrix[0]) == len(matrix[0]) else False


class Processor:
    m1 = Matrix()
    m2 = Matrix()
    m3 = m1 + m2
    print(m3)


if __name__ == '__main__':
    start = time()
    processor = Processor()
    end = time()
    print(f'time taken {end - start}')