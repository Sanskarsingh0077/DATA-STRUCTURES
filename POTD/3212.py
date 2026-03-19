class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])


        csumX = [[0]*(cols) for _ in range(rows)]
        csumY = [[0]*(cols) for _ in range(rows)]

        count = 0
        for i in range(rows):
            for j in range(cols):


                csumX[i][j] = (grid[i][j] == 'X')
                csumY[i][j] = (grid[i][j] == 'Y')


                if i-1 >= 0:
                    csumX[i][j] += csumX[i-1][j]
                    csumY[i][j] += csumY[i-1][j]

                if j-1 >= 0:
                    csumX[i][j] += csumX[i][j-1]
                    csumY[i][j] += csumY[i][j-1]

                if i-1 >= 0 and j-1 >= 0:
                    csumX[i][j] -= csumX[i-1][j-1]
                    csumY[i][j] -= csumY[i-1][j-1]


                if (csumX[i][j] == csumY[i][j]) and (csumX[i][j] > 0):
                    count += 1

        return count