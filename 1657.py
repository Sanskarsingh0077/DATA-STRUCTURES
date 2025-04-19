class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
'''
    Approach:
    1. Check if the lengths of the two strings are equal. If not, return False.
    2. Create two frequency maps (dictionaries) to count occurrences of each character in both strings.
    3. Compare the sets of keys from both maps to ensure both strings use the same set of characters.
    4. Compare the sorted lists of frequency values from both maps to verify character counts can be rearranged.
    5. If both the character sets and the frequency distributions match, return True; otherwise, return False.

    # Note on Space Complexity:
    - Current space complexity is O(k), where k is the number of unique characters (up to 26 for lowercase English).
    - If using fixed-size arrays instead of maps (assuming only lowercase letters), space can be optimized to O(1).
    - To do this, replace the dictionaries with arrays of size 26 using index mapping (ord(char) - ord('a')).

'''
        if len(word1) != len(word2):
            return False

        map1 = {}
        map2 = {}

        for i in word1:
            map1[i] = map1.get(i,0)+1
        
        for i in word2:
            map2[i] = map2.get(i,0)+1

        if set(map1.keys()) != set(map2.keys()):
            return False
        
        if sorted(map1.values()) != sorted(map2.values()):
            return False
        
        return True
