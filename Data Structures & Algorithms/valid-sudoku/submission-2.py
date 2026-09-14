class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowsLen = len(board)
        colsLen = len(board[0])

        # Creating 3 sets for storing if the particular value is there or not
        rows = collections.defaultdict(set) #key -> index; value -> set
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(rowsLen):
            for c in range(colsLen):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True