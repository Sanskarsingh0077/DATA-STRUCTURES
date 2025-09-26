class Solution:
    #Brute Force : O(n^3)
    #Using Sorting O(n^2*logn)
    '''
    def binarysearch(self,nums, l,r , target):
        
        k = -1

        while l<= r:
            mid = l + (r-l)//2

            if nums[mid] < target:
                k = mid
                l = mid +1

            else:
                r = mid -1

        return k

    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        if n < 3:
            return 0

        count = 0

        for i in range(n):
            if nums[i] == 0:
                continue
            
            for j in range(i+1,n):
                sums = nums[i] + nums[j]

                k = self.binarysearch(nums,j+1,n-1, sums)

                if k != -1:
                    count += (k - j)

        return count
        '''

    # Most Optimal Solution two pointer O(n^2)
    def triangleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n < 3:
            return 0

        nums.sort()

        count = 0

        for k in range(n-1,1,-1):
            i = 0
            j = k -1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j-i)
                    j -= 1

                else:
                    i +=1

        return count