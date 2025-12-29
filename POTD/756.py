class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)

        for pattern in allowed:
            mp[pattern[:2]].append(pattern[2]) # "ab -> c"
        print(mp)

        def solve(curr, mp, idx, above):
            if len(curr) == 1:
                return True

            if idx == len(curr) - 1:
                return solve(above, mp, 0, "")

            pair = curr[idx:idx+2]

            if pair not in mp:
                return False

            for char in mp[pair]:
                
                if solve(curr, mp, idx+1, above + char): # Do and Explore
                    return True 

            return False

        
        return solve(bottom, mp, 0, "")


