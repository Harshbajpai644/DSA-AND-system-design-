class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            word_weight = 0
            for char in word:
                word_weight += weights[ord(char) - ord('a')]
            
            remainder = word_weight % 26
            mapped_char = chr(ord('z') - remainder)
            result.append(mapped_char)
            
        return "".join(result)
