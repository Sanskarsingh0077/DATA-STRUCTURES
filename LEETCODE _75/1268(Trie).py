class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Trie Approach: 
        products.sort() # Sort to make sure suggestions are lexicographically smallest

        root = TrieNode()

         # Build Trie
        for product in products:
            node = root
            for ch in product:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                
                node = node.children[ch]

                if len(node.suggestions) < 3:
                    node.suggestions.append(product)

        
        result = []
        node = root
        # Get suggestions for each prefix
        for ch in searchWord:
            if ch in node.children:
                node = node.children[ch]
                result.append(node.suggestions)
            
            else:
                while len(result) < len(searchWord):
                    result.append([])
                break

        return result

        #Two Pointer approach

        result = []
        products.sort()

        left = 0
        right = len(products) - 1

        for i in range(len(searchWord)):
            c = searchWord[i]

            while left <= right and (len(products[left])<= i or products[left][i] != c):
                left += 1

            while left <= right and (len(products[right])<=i or products[right][i] != c):
                right -= 1

            result.append([])
            remain = right - left + 1
            for j in range(min(3,remain)):
                result[-1].append(products[left + j])

        
        return result

'''
        Approach: Two Pointers + Sorting
        1.	Sort the products list lexicographically.
        2.	Initialize two pointers: left and right to cover the full range of products.
        3.	For each character in searchWord:
        •	Narrow the range by moving left and right so that only products starting with the current prefix remain.
        4.	From the current valid range (left to right), pick up to the first 3 matching products and add them to the result.
        5.	Repeat for each prefix formed by typing one more character of searchWord.
    
'''
    
        #Sorting + Binary Search (Very Efficient and Simple)

        products.sort()
        result = []
        prefix = ""
        
        for ch in searchWord:
            prefix += ch
            i = bisect_left(products, prefix)  # find where prefix would start
            suggestions = []
            
            # Take up to 3 suggestions starting from i
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
            result.append(suggestions)
        
        return result

'''
        Approach:

            1.	Sort the products list lexicographically.
            2.	For each prefix of searchWord, use binary search to find the first product ≥ prefix.
            3.	From there, take the next 3 products (if they match the prefix).
        
'''

