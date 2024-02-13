class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix) 
        cols = len(matrix[0]) 
        
        output = []
        
        row_begin = 0
        col_begin = 0
        row_end = rows - 1
        col_end = cols - 1

        while row_begin <= row_end and col_begin <= col_end:
            #move right
            for j in range(col_begin, col_end + 1):
                cell = matrix[row_begin][j]
                output.append(cell)
            row_begin += 1
            if row_begin > row_end:
                break
            
            #move down
            for i in range(row_begin, row_end + 1):
                cell = matrix[i][col_end]
                output.append(cell)
            col_end -= 1
            if col_begin > col_end:
                break

            #move left
            for j in range(col_end, col_begin - 1, -1):
                cell = matrix[row_end][j]
                output.append(cell)
            row_end -= 1
            if row_begin > row_end:
                break

            #move upwards
            for i in range(row_end, row_begin - 1, -1):
                cell = matrix[i][col_begin]
                output.append(cell)
            col_begin += 1
            if col_begin > col_end:
                break

        return output

            

            


        