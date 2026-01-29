from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        inf = float('inf')
        flyodmatrix = [[inf]*26 for _ in range(26)]
        
        for i in range(26):
            flyodmatrix[i][i] = 0
            
        
        for o, c, cost in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            
            flyodmatrix[u][v] = min(flyodmatrix[u][v], cost)
            
        
        #Floydd Warshall Logic Begin Updating created floydd matrix
        
        for via in range(26):
            for i in range(26):
                for j in range(26):
                    flyodmatrix[i][j] = min(flyodmatrix[i][j], flyodmatrix[i][via]+flyodmatrix[via][j])
                    
        
        # Start Comparing each character
        final_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            
            
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            
            if flyodmatrix[u][v] == inf:
                return -1
            
            final_cost += flyodmatrix[u][v]
            
        return final_cost
    
    
            
print(Solution().minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]))