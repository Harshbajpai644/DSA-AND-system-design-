class Solution:
    def minOperations(self, s: str) -> int:
        count0 = 0
        n = len(s)
        
        for i in range(n):
            if i % 2 == 0:
                if s[i] != '0':
                    count0 += 1
            else:
                if s[i] != '1':
                    count0 += 1
        
        return min(count0, n - count0)