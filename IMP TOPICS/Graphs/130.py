class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        def capture(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return 

            # Change O -> T in edges
            board[r][c] = "T"

            #Visit Directions
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)

        # 1: Capture Unsorrounded regoins "O" -> "T" (DFS)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and ((r in [0, rows-1] or c in [0, cols - 1])):
                    capture(r,c)
           
 
        # 2 : Capture Surrounded Region "O" -> "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"


        # 3 : Uncapture Unsurrounded regions "T" -> "O"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"



        
