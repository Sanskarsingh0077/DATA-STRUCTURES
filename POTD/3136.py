class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set('aeiouAEIOU')

        is_vowel = False
        is_consonant = False

        if len(word) < 3:
            return False

        for ch in word:
            if not ch.isalnum(): # Not a letter or digit
                return False

            if ch.isalpha():
                if ch in vowels:
                    is_vowel = True
                else:
                    is_consonant = True

        return is_vowel and is_consonant

        # Time Complexity: O(n) → can’t improve further, must scan the word.
        # Space Complexity: O(1) → optimal, uses no extra space that scales with input.