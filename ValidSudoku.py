class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            # check rows
            flag = [0 for k in range(9)]
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif flag[int(board[i][j]) - 1] == 0:
                    flag[int(board[i][j]) - 1] = 1
                else:
                    return False

            #check colume
            flag = [0 for k in range(9)]
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif flag[int(board[j][i]) - 1] == 0:
                    flag[int(board[j][i]) - 1] = 1
                else:
                    return False

        #check boxes
        for i in range(7):
            for j in range(7):
                flag = [0 for k in range(9)]
                if i % 3 == 0 and j % 3 == 0:
                    for x in range(3):
                        for y in range(3):
                            if board[i + x][j + y] == '.':
                                continue
                            elif flag[int(board[i + x][j + y]) - 1] == 0:
                                flag[int(board[i + x][j + y]) - 1] = 1
                            else:
                                return False
        return True

sol = Solution()
board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print sol.isValidSudoku(board)
        