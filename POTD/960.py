class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        # LIS Variant

        cols = len(strs[0])
        rows = len(strs)

        dp = [1]*(cols)
        LIS = 0

        for i in range(cols):
            for j in range(i):
                valid = True
                for r in range(rows):
                    if strs[r][j] > strs[r][i]:
                        valid = False
                        break

                if valid:
                    dp[i] = max(dp[i], dp[j]+ 1)

            LIS = max(LIS, dp[i])

        return cols - LIS

