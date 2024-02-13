class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def makezero(zero):
            i, j = zero
            for row in range(0, len(matrix)):
                matrix[row][j] = 0
            for col in range(0, len(matrix[0])):
                matrix[i][col] = 0
        zeroes = []
        rows = len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append((i,j))
        for zero in zeroes:
            makezero(zero)

                 
        