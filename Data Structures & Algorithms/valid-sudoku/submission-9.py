class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                
                if board[r][c] == ".":
                    continue
                
                v = board[r][c]

                if v in rows[r] or v in cols[c] or v in squares[(r // 3, c // 3)]:
                    return False
                else:
                    rows[r].add(v)
                    cols[c].add(v)
                    squares[(r // 3, c // 3 )].add(v)
        return True