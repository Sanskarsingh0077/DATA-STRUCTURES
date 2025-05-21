class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        map_s ={} 
        '''
        Approach 1: Iteratively storing in map.

        for ch in s:
            if ch in map_s:
                map_s[ch] += 1
            else:                       
                map_s[ch] = 1

        '''

        #Approach 2: Storing using get

        for ch in s:
            map_s[ch] = map_s.get(ch, 0) + 1


        
        frequencies = list(map_s.values()) #Convert values in a list

        return len(set(frequencies)) == 1 #if all frequencies are the same, the set will contain only one unique value.


        #freq_map[ch] = freq_map.get(ch, 0) + 1 
