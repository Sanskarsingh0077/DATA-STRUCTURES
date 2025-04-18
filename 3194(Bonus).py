class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        avg_arr=[]

        i=0
        j=len(nums)-1

        while i < j:
            averages =(nums[i]+nums[j])/2
            avg_arr.append(averages)
            i+=1
            j-=1


        return min(avg_arr)
    

    '''
    Space Complexity Improved:
    Make changes in the original nums array brings down space from O(n)
    to O(1). No extra array.


    nums.sort()
        #avg_arr=[]

        i=0
        j=len(nums)-1

        while i <= j:
            nums[i] =(nums[i]+nums[j])/2
            #avg_arr.append(averages)
            i+=1
            j-=1


        #return min(nums)
        return min(nums[: (len(nums) + 1) // 2])
    
    '''