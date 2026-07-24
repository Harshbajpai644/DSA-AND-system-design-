class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        n = len(unique_nums)
        
        s2 = set()
        for i in range(n):
            for j in range(i, n):
                s2.add(unique_nums[i] ^ unique_nums[j])
                
        s3 = set()
        for x in s2:
            for y in unique_nums:
                s3.add(x ^ y)
                
        return len(s3) 