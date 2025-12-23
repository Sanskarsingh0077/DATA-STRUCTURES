class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col = len(strs[0])
        row = len(strs)

        ok = [False] * (row-1)
        res = 0

        for c in range(col):
            deleted = False
            for r in range(row-1):
                if not ok[r] and strs[r][c] > strs[r+1][c]:
                    deleted = True
                    res += 1
                    break

            if not deleted:
                for r in range(row - 1):
                    if strs[r][c] < strs[r+1][c]:
                        ok[r] = True


        return res

    
    #TC : O(rows x Cols)