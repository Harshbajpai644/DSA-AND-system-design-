class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        
        
        blocks = []
        i = 0
        n = len(s)
        
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            blocks.append((s[i], j - i))
            i = j
            
        max_delta = 0
        m = len(blocks)
        
        for k in range(m):
            char, length = blocks[k]
            if char == '1':
                
                if k > 0 and k < m - 1:
                    left_zero_len = blocks[k - 1][1]
                    right_zero_len = blocks[k + 1][1]
                    
                    delta = left_zero_len + right_zero_len
                    if delta > max_delta:
                        max_delta = delta

        return initial_ones + max_delta