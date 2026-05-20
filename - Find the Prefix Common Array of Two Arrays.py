class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n
        frequency = [0] * (n + 1)
        common_count = 0
        
        for i in range(n):
            frequency[A[i]] += 1
            if frequency[A[i]] == 2:
                common_count += 1
                
            frequency[B[i]] += 1
            if frequency[B[i]] == 2:
                common_count += 1
                
            C[i] = common_count
            
        return C
