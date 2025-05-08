class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        ''' 
        Leetcode 1456. Max number of vowels in a substring of given length.

        Logic

        1.) i=0,j=0->for two ends of our window

        2.) Keep counting vowel if s[j] is 'a' or 'e' or 'i' or 'o' or 'u'

        3.) when reach window of size k i.e. (j+1-i==k):
            Update maxV
            Shift window right side (i++) but also adjust vowel count if(s[i] was a vowel)

        '''
                
        count=0
        i=0
        j=0
        maxV=0
        n=len(s)

        vowels=['a','e','i','o','u','A','E','I','O','U']

        for j in range(n):
            if s[j] in vowels:
                count+=1
                
            if j+1-i == k:
                maxV= max(maxV,count)
                if s[i]  in vowels:
                    count-=1
                i+=1


        return maxV