import collections
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        index_map = collections.defaultdict(list)
        
        for idx, val in enumerate(nums):
            index_map[val].append(idx)
            
        answer = []
        for q_idx in queries:
            val = nums[q_idx]
            indices = index_map[val]
            
            if len(indices) == 1:
                answer.append(-1)
                continue
            
            pos = bisect.bisect_left(indices, q_idx)
            
            left_idx = indices[pos - 1]
            right_idx = indices[(pos + 1) % len(indices)]
            
            dist_left = min(abs(q_idx - left_idx), n - abs(q_idx - left_idx))
            dist_right = min(abs(q_idx - right_idx), n - abs(q_idx - right_idx))
            
            answer.append(min(dist_left, dist_right))
            
        return answer
