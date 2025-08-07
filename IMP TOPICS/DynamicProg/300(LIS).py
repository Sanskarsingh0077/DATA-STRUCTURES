class Solution:
    import bisect
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Top Down Memoization : TLE in python
        
        n = len(nums)

        dp = [[-1] * (n + 1) for _ in range(n+1)]

        def solve(index,prev):
            if index >= n:
                return 0
            
            if prev != -1 and dp[index][prev+1] != -1:
                return dp[index][prev+1]

            take = 0
            if prev == -1 or nums[prev] < nums[index]:
                take = 1 + solve(index+1,index)

        
            skip = solve(index+1, prev)

            if prev != -1:
                dp[index][prev+1] = max(take,skip)
                return dp[index][prev+1]
                

            return max(take,skip)
            

        return solve(0,-1)
        

        # Bottom Up 

       

        n = len(nums)
        t = [1]*(n)
        maxLIS = 1

        for i in range(0,n):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    t[i] = max(t[i],t[j]+1)
                    maxLIS = max(maxLIS,t[i])

        return maxLIS

        

        #Lazy Sorting (O(n log n))
      
        n = len(nums)

        new = []
        
        for num in nums :
            idx = bisect.bisect_left(new,num) # Find the index of the first element in sorted_list >= num

            if idx == len(new):
                new.append(num)  # num is greater than all elements so far

            else:
                new[idx] = num # replace the element at idx

        return len(new)

        


        #Binary Search + Greedy (Manually writing binary search)

        def binary(new,target):
            low = 0
            high = len(new)-1

            while high >= low:
                mid = (low + high) // 2

                if new[mid] < target:
                    low = mid + 1

                else:
                    high = mid -1
            return low

        new = []

        for num in nums:
            pos = binary(new,num)

            if pos == len(new):
                new.append(num)

            else:
                new[pos] = num

        return len(new)

        


