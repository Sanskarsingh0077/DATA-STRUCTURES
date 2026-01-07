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





        


