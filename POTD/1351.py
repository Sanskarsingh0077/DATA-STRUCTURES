class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Brute Force [ O(m * n)]
        '''
        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    res += 1

        return res
        '''

        # Using Binary Search (O(m * logn))
        '''
        n = len(grid[0])

        def binary_search(row):
            left = 0
            right = n-1

            ans = n

            while left <= right:
                mid = (left + right)//2

                if row[mid] < 0:
                    ans = mid
                    right = mid - 1
                
                else:
                    left = mid + 1

            return ans

        count = 0

        for row in grid:
            idx = binary_search(row)

            count += n - idx

        return count 

        '''

        # Best Approach [ O(m + n ) ]

        m = len(grid)
        n = len(grid[0])

        col = 0
        row = m -1

        res = 0

        while row >= 0 and col < n:
            if grid[row][col] >= 0:
                col += 1

            else:
                res += n - col
                row -= 1

        return res

        

