class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
            else:
                
                lowest_zero = (~x) & -(~x)
                
              
                bit_to_unset = lowest_zero >> 1
                
                ans.append(x ^ bit_to_unset)
        return ans
