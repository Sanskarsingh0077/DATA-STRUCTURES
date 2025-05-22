class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        def build_word_map(sentence):
            word_map = {}
            for word in sentence.split():
                if word in word_map:
                    word_map[word] += 1
                else:
                    word_map[word] = 1
            return word_map

        def store_unique(from_map,other_map,result):
            for word in from_map:
                if word not in other_map and from_map[word] == 1:
                    result.append(word)

        map_s1 = build_word_map(s1)
        map_s2 = build_word_map(s2)

        unique_only = []

        store_unique(map_s1,map_s2, unique_only)
        store_unique(map_s2,map_s1, unique_only)

        return unique_only        

        

        


        