class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        '''
        dp = [-1]*n

        def solve(idx):
            
            if idx>=n:
                return 0

            if dp[idx] != -1:
                return dp[idx]

            pick = nums[idx]+solve(idx+2) #Pick alternate House
            skip = solve(idx+1) #Skip next house if looted one, ex: if looted House 1 Skip House 2

            dp[idx]= max(skip,pick) 
            return dp[idx]

        return solve(0)
        '''

        house = [0]*(n+1) #dp[i] - Max loot from the first i houses


        if n ==1 :
            return nums[0]

        house[0]=0
        house[1] = nums[0]


        for i in range(2, n+1):
            pick = nums[i-1] + house[i-2] #	Rob it: take nums[i-1] + dp[i - 2] (because i-1 is skipped)
            skip = house[i-1] #	Skip it: loot stays dp[i - 1]

            house[i] = max(pick,skip) 	#Pick whichever gives more money. dp[i] represents the max loot you can collect up to house i.
        
        return house[n] #dp[n] ✅ Final result: max loot from all houses (if properly filled)


        
        