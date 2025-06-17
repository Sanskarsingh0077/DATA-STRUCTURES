class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])

        count = 0
        prev_interval = intervals[0][1]


        for i in range(1,len(intervals)):
            if intervals[i][0] < prev_interval:
                count +=1

            else:
                prev_interval = intervals[i][1]

        return count

        '''
        Approach:

        Greedy Approach (Optimal)
        1.	Sort all intervals by their end time — This helps us always keep the interval that ends the earliest (to leave more space for the next intervals).
        2.	Initialize prev_end with the end time of the first interval.
        3.	Iterate from the second interval onward:
        •	If the current interval starts before prev_end, it overlaps, so remove it (increment count).
        •	If it does not overlap, keep it and update prev_end to this interval’s end time.
	    4.	Return count, which is the minimum number of intervals you need to remove to eliminate all overlaps.

        Time Complexity: O(n log n)
        Space Complexity: O(1)

        '''