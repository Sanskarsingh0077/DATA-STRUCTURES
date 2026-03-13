class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        # Brute Force
        '''
        res = float('-inf')
        array = []

        for i in range(len(arr)):
            for j in range(1, len(arr)):
                array.append(arr[i:j+1])

        def is_alternating(arr):
            n = len(arr)

            big_small = True
            small_big = True

            for i in range(1, n):
                if i % 2 == 1:
                    if arr[i-1] <= arr[i]:
                        big_small = False
                    if arr[i-1] >= arr[i]:
                        small_big = False
                else:
                    if arr[i-1] >= arr[i]:
                        big_small = False
                    if arr[i-1] <= arr[i]:
                        small_big = False

            return big_small or small_big

        for i in array:
            if is_alternating(i):
                if len(i) > res:
                    res = len(i)

        return res if res != float('-inf') else 1

        '''

        #Sliding Window O(n) -- Solution
        l , r = 0, 1
        res = 1
        prev = ''

        while r < len(arr):
            # Case 1 Exapand Window (Condition True)
            if arr[r-1] > arr[r] and prev != '>':
                res = max(res, r - l + 1)
                r += 1
                prev = '>'

            # Case 2 Expand Window (Condition True)
            elif arr[r-1] < arr[r] and prev != '<':
                res = max(res, r - l + 1)
                r += 1
                prev = '<'

            # Case 3 (Condition False)
            else:
                # Move Right if both equals
                if arr[r-1] == arr[r]: 
                    r += 1

                # Shrink Window
                l = r - 1
                prev = ''


        return res

            




        
        

    
                
                