class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagram(word1,word2):
            return sorted(word1) == sorted(word2)

        n = len(words)
        res = [words[0]]

        for i in range(1,n):
            if not isAnagram(words[i],words[i-1]):
                res.append(words[i])

        return res