class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = (1 << n) - 1
        mid = (length // 2) + 1
        
        if k < mid:
            return self.findKthBit(n - 1, k)
        elif k == mid:
            return "1"
        else:
            
            corresponding_k = length - k + 1
            res = self.findKthBit(n - 1, corresponding_k)
            return "1" if res == "0" else "0"