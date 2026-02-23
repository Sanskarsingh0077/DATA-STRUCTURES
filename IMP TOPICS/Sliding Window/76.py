class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Brute Force ---> O(n * n * n) ~ O(n^3)

        '''

        def isValid(str1, str2): # O(n)
            mp1 = {}

            for i in str1:
                if i in mp1:
                    mp1[i] += 1
                else:
                    mp1[i] = 1

            for ch in str2:
                if ch not in mp1 or mp1[ch] == 0:
                    return False
                else:
                    mp1[ch] -= 1

            return True


        n = len(s)
        mini = float('inf')

        ans = ""

        for i in range(n): #O(n)
            for j in range(i, n): # O(n)
                substr = s[i: j+1]

                if isValid(substr, t):
                    if len(substr) < mini:
                        mini = len(substr)
                        ans = substr

        return ans
        '''

        #Optimization - Sliding Window O(n)
        have = 0
        
        need = {}
        

        res_len = float('inf')
        res = [-1,-1]

        left = 0

        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        req = len(need)

            # need[ch] = need.get(ch, 0) + 1

        window = {}

        for right in range(len(s)):
            ch = s[right]

            if ch in window:
                window[ch] += 1
            
            else:
                window[ch] = 1

            
            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == req:
                # Update Answer
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = [left, right]

                #Shrink Window

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1


        l,r = res

        return s[l:r+1] if res_len != float('inf') else ""
    
    
    '''
    
    class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = {ch : 0 for ch in string.ascii_letters} # Store all Letters in dic ch : freq

        # Increase freq as per t string
        for i in t:
            if i not in hashmap:
                hashmap[i] = 0

            hashmap[i] += 1

        left = 0
        right = 0
        minlength = float('inf')
        startIndex = -1

        n = len(s)
        m = len(t)
        count = 0

        while right < n:
            # Start checking in s 
            if hashmap[s[right]] > 0:
                count += 1
            hashmap[s[right]] -= 1


            while count == m:
                # update min length 
                if right - left + 1 < minlength:
                    minlength = right - left + 1
                    startIndex = left

                # Shrink left pointer
                hashmap[s[left]] += 1
                if hashmap[s[left]] > 0:
                    count -= 1

                left += 1
            # Expand Window
            right += 1

        
        return "" if startIndex == -1 else s[startIndex: startIndex + minlength]



    
    '''





        


