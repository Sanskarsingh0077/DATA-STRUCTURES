def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        '''
        #Top Down Memoization

        m = 10**9+7

        dp = [-1]*(n+1)

        def solve(day):
            if day == 1:
                return 1

            if dp[day] != -1:
                return dp[day]

            res = 0
            for prev in range(day-forget+1, day-delay+1):
                if prev>0:
                    res = (res + solve(prev))%m
            
            dp[day] = res
            return dp[day]

        total = 0
        for day in range(n-forget+1,n+1):
            if day>0:
                total = (total + solve(day))%m

        return total


        Time Complexity: O(n*(forget-delay))
        Space Complexity: O(n) -- Creating dp Array of n
        '''

        #Bottom Up 

        m = 10**9+7

        t = [0]*(n+1)

        t[1] = 1

        for day in range(2,n+1):
            count = 0
            for prev in range(day-forget+1, day-delay+1):
                count = (count + t[prev])%m

            t[day] = count

        res = 0
        for day in range(day-forget+1, n+1):
            if day>0:

                res = (res + t[day])%m

        return res