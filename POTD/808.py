#808. Soup Servings (Logical Question)

def soupServings(self, n: int) -> float:
        serves = [[100,0],[75,25],[50,50],[25,75]] #Cases

        if n >= 5000:  #Stop Early if found as n value increases probability of b ending decreases, and a comes close to 1.
            return 1.0

        dp = [[-1]*(n+1) for _ in range(n+1)]

        def solve(a,b):
            if a <= 0 and b <= 0:
                return 0.5

            if a <= 0:
                return 1.0

            if b <= 0:
                return 0.0

            if dp[a][b] != -1:
                return dp[a][b]

            prob = 0

            for p in serves:
                a_taken = p[0]
                b_taken = p[1]

                prob += solve(a-a_taken,b-b_taken)

            dp[a][b] = 0.25 * prob
            return dp[a][b]
            
        return solve(n,n)