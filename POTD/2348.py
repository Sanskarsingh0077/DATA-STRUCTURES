def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        streak = 0

        for num in nums:
            if num == 0:
                streak += 1
                count += streak

            else:
                streak = 0


        return count
    
    
'''
Java Code

class Solution {
    public long zeroFilledSubarray(int[] nums) {
        int count = 0;
        int streak = 0;

        for(int num : nums){
            if(num == 0){
                streak++;
                count += streak;
            }else streak = 0;
            
        }
        return count;
    }
}
    
'''