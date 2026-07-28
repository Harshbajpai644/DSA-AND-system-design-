class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        left,right= 0,n-1
        for i in range (n-1,-1,-1):
            left_square = nums[left]**2
            right_square = nums[right]**2


            if left_square>right_square:
                result[i] = left_square
                left += 1
            else:
                result[i] = right_square
                right -= 1
        return result
        