class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic Decreasing Deque
        
        right , left = 0 , 0
        res = []
        q = deque()

        while right < len(nums):

            # Maintain decreasing order
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            # Remove elements out of window
            if left > q[0]:
                q.popleft()

            # When window size becomes k
            if right >= k -1:
                res.append(nums[q[0]])
                left += 1

            right += 1

        return res

        #TC : O(n)
