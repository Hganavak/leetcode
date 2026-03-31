class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # Cols
       for x in range(9):
        col={}
        for y in range(9):
            v = board[x][y]

            if v.isnumeric():
                if v in col:
                    return False

                col[v] = True

       # Rows
       for y in range(9):
        row={}
        for x in range(9):
            print('row: ', x, y, row)
            v = board[x][y]

            if v.isnumeric():
                row[v] = row.get(v, 0) + 1

                if row[v] > 1:
                    print('FALSE (row)')
                    return False

       # Nines 
       for x in range(3):
        for y in range(3): # The 3x3 grid

            grid={}

            startingX = x * 3 # So if x = 2, startingX = 6
            startingY = y * 3 # So if y = 0, startingY = 0

            print('Grid search starting at', startingX, startingY)

            for innerX in range(3):
                for innerY in range(3):
                    
                    v = board[startingX + innerX][startingY + innerY]
                    print('\tLooking at value at', startingX + innerX, startingY + innerY, 'which equals: ', v)

                    if v.isnumeric():
                        grid[v] = grid.get(v, 0) + 1

                        if grid[v] > 1:
                            print('FALSE (grid)')
                            return False

       return True