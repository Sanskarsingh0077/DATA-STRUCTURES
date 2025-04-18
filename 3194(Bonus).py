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