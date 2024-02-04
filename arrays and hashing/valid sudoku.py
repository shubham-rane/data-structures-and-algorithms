class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        positions = set()
        count = -1
        squares = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                count = count+1
                if board[i][j] != ".":
                    # oglen = len(positions)
                    # positions.add(str(board[i][j])+"r"+str(i))
                    # if len(positions) == oglen:
                    #     return False
                    # oglen = len(positions)
                    # positions.add(str(board[i][j])+"c"+str(j))
                    # if len(positions) == oglen:
                    #     return False
                    # oglen = len(positions)
                    # positions.add(str(board[i][j])+"e"+str(int(i//3))+str(int(j//3)))
                    # if len(positions) == oglen:
                    #     return False

                    
                    if (str(board[i][j])+"r"+str(i)) not in positions:
                        positions.add(str(board[i][j])+"r"+str(i))
                    else:
                        return False
                    
                    if (str(board[i][j])+"c"+str(j)) not in positions:
                        positions.add(str(board[i][j])+"c"+str(j))
                    else:
                        return False
                    
                    if (str(board[i][j])+"e"+str(int(i//3))+str(int(j//3))) not in positions:
                        positions.add(str(board[i][j])+"e"+str(int(i//3))+str(int(j//3)))
                    else:
                        return False
                           
        return True
                    

        