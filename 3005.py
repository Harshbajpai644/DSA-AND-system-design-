from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_freq = 0
        
        for freq in counts.values():
            if freq > max_freq:
                max_freq = freq
        
        total_max_freq_elements = 0
        for freq in counts.values():
            if freq == max_freq:
                total_max_freq_elements += max_freq
                
        return total_max_freq_elements