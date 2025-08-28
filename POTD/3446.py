class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        n = len(grid)

        def sortDiagonal(row, col, grid, ascending):
            vec = []

            i = row
            j = col

            while(i<n and j<n):
                vec.append(grid[i][j])
                i += 1
                j += 1

            if ascending:
                vec.sort()
            else:
                vec.sort(reverse= True)

            i = row
            j = col
            for val in vec:
                grid[i][j] = val
                i += 1
                j += 1

        # Bottom Left - Non Increasing Order
        for row in range(n):
            sortDiagonal(row, 0 , grid, False)

        #Top- Right - Increasing Order

        for col in range(1,n):
            sortDiagonal(0, col , grid, True)

        return grid
        '''

        #Using Hash Maps

        n= len(grid)
        mp = {}

        for i in range(n):
            for j in range(n):
                if i-j not in mp:
                    mp[i-j] = []

                mp[i-j].append(grid[i][j])

        for key,val in mp.items():
            if key>=0:
                val.sort()

            else:
                val.sort(reverse = True)

        for i in range(n):
            for j in range(n):
                diag = i - j
                grid[i][j] = mp[diag][-1] # Get Last element from the sorted list
                mp[diag].pop() # Removing the used element


        return grid