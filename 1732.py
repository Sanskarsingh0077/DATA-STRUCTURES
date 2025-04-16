class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        altitude = 0

        for i in gain:
            altitude+=i
            max_altitude = max(max_altitude,altitude)

        return max_altitude


        
        '''
        Approach:
        
        # Initialize max_altitude and current altitude
        # Loop through each gain in the journey
        #   - Update current altitude by adding the gain
        #   - Update max_altitude if current altitude is higher
        # Return the highest altitude reached

        '''