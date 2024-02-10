class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # transpose

        for i in range(0, len(matrix)):
            for j in range(i+1, len(matrix)):
                #temp = matrix[i][j]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse
        for row in matrix:
            row.reverse()
            
            
        