class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        '''
        # Default dict()
        mp = defaultdict(list)

        for pattern in allowed:
            mp[pattern[:2]].append(pattern[2]) # "ab -> c"
        print(mp)

        '''
        # Manual Map Creation
        mp = {}

        for pattern in allowed:
            key = pattern[:2]
            val = pattern[2]

            if key not in mp:
                mp[key] = []

            mp[key].append(val)

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

        # TC : O( L ^ n )


