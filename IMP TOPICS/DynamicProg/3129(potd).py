class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        '''
        dp = [[[-1] * 2 for _ in range(zero+1)] for _ in range(one+1)]

        def solve(onesleft:int, zeroesleft:int, lastusedone:bool):
            
            # Base Case
            if onesleft == 0 and zeroesleft == 0:
                return 1
            
            # Memoization
            if dp[onesleft][zeroesleft][lastusedone] != -1:
                return dp[onesleft][zeroesleft][lastusedone]

            res = 0
            # Use Zero
            if lastusedone:
                for l in range(1,min(limit, zeroesleft)+1):
                    res += solve(onesleft, zeroesleft - l, False)
            # Use one
            else:
                for l in range(1,min(limit, onesleft) + 1):
                    res += solve(onesleft - l, zeroesleft, True)

            dp[onesleft][zeroesleft][lastusedone] = res
            return dp[onesleft][zeroesleft][lastusedone]


        startwithone = solve(one, zero, False)
        startwithzero = solve(one, zero, True)

        return (startwithone + startwithzero)%mod

        '''

        # Bottom Up Approach
        t = [[[-1] * 2 for _ in range(zero + 1)] for _ in range(one+1)]
        t[0][0][0] = 1
        t[0][0][1] = 1
        for onesleft in range(one+1):
            for zeroesleft in range(zero+1):
                if onesleft == 0 and zeroesleft == 0:
                    continue

                res = 0
                for l in range(1,min(limit, zeroesleft)+1):
                    res = (res + t[onesleft][zeroesleft-l][0])%mod

                t[onesleft][zeroesleft][1] = res

                res = 0
                for l in range(1,min(limit, onesleft)+1):
                    res = (res + t[onesleft-l][zeroesleft][1])%mod

                t[onesleft][zeroesleft][0] = res

        return (t[one][zero][0] + t[one][zero][1])%mod

