class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s: str, a: str, b: str, gain: int) -> (str, int):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    score += gain
                else:
                    stack.append(ch)
            return ''.join(stack), score

        # Decide which pair to remove first
        if x > y:
            s, score1 = remove_pairs(s, 'a', 'b', x)
            s, score2 = remove_pairs(s, 'b', 'a', y)
        else:
            s, score1 = remove_pairs(s, 'b', 'a', y)
            s, score2 = remove_pairs(s, 'a', 'b', x)

        return score1 + score2