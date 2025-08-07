def numOfArrays(self, n: int, m: int, k: int) -> int:
        # Initialize 3D DP table with -1 (or any default value)
        dp = [[[-1]*(m+1) for _ in range(k+1)] for _ in range(n+1)]
        MOD = 10**9 + 7

        def solve(index,search_cost,maxelement):
            if search_cost > k:
                return 0

            if index == n:
                if search_cost == k:
                    return 1
                
                else:
                    return 0

            if dp[index][search_cost][maxelement] != -1:
                return dp[index][search_cost][maxelement]
            
            result = 0
            for i in range(1,m+1):
                if i > maxelement:
                    result += solve(index+1 , search_cost +1 , i)

                else:
                    result += solve(index+1, search_cost, maxelement)

            dp[index][search_cost][maxelement] = result % MOD

            return dp[index][search_cost][maxelement]

        return solve(0,0,0)