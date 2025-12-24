class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()

        count = 0
        dp = {}

        def binarySearch(val):
            l = 0
            r = n -1 
            res = n

            while l <= r:
                mid = l + (r-l)//2

                if events[mid][0] > val:
                    res = mid
                    r = mid -1
                else:
                    l = mid + 1

            return res


        def solve(idx, count):
            if count == 2 or idx >= n:
                return 0

            if (idx, count) in dp:
                return dp[(idx,count)]

            nextValidIndex = binarySearch(events[idx][1])
            take = events[idx][2] + solve(nextValidIndex, count+1)
            skip = solve(idx+1, count)

            dp[(idx, count)] = max(take, skip)

            return dp[(idx, count)]

        return solve(0, count)
