class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        indices_map = collections.defaultdict(list)
        
        for i, val in enumerate(nums):
            indices_map[val].append(i)
            
        for val in indices_map:
            indices = indices_map[val]
            m = len(indices)
            
            total_sum = sum(indices)
            prefix_sum = 0
            
            for i, idx in enumerate(indices):
                suffix_sum = total_sum - prefix_sum - idx
                
                left_count = i
                right_count = m - 1 - i
                
                left_total = (left_count * idx) - prefix_sum
                right_total = suffix_sum - (right_count * idx)
                
                ans[idx] = left_total + right_total
                prefix_sum += idx
                
        return ans
