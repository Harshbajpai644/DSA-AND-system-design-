class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        max_dist = 0
        n1, n2 = len(nums1), len(nums2)
        
        for j in range(n2):
            while i < n1 and nums1[i] > nums2[j]:
                i += 1
            
            if i < n1 and i <= j:
                max_dist = max(max_dist, j - i)
                
        return max_dist
