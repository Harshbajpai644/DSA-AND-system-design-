from collections import deque

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        max_val = max(nums)
        # Sieve to find primes and prime factors
        spf = list(range(max_val + 1))
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(max_val**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, max_val + 1, i):
                    is_prime[j] = False
                    if spf[j] == j:
                        spf[j] = i

        # bucket[p] stores all indices j where nums[j] % p == 0
        prime_to_indices = {}
        for i, val in enumerate(nums):
            temp = val
            visited_factors = set()
            while temp > 1:
                p = spf[temp]
                if p not in visited_factors:
                    if p not in prime_to_indices:
                        prime_to_indices[p] = []
                    prime_to_indices[p].append(i)
                    visited_factors.add(p)
                while temp % p == 0:
                    temp //= p
        
        queue = deque([(0, 0)])
        visited_indices = {0}
        used_prime_portals = set()
        
        while queue:
            idx, dist = queue.popleft()
            
            if idx == n - 1:
                return dist
            
            # 1. Adjacent Steps
            for neighbor in [idx - 1, idx + 1]:
                if 0 <= neighbor < n and neighbor not in visited_indices:
                    if neighbor == n - 1: return dist + 1
                    visited_indices.add(neighbor)
                    queue.append((neighbor, dist + 1))
            
            # 2. Prime Teleportation (ONLY if nums[idx] is prime)
            p = nums[idx]
            if p <= max_val and is_prime[p] and p not in used_prime_portals:
                if p in prime_to_indices:
                    for next_idx in prime_to_indices[p]:
                        if next_idx not in visited_indices:
                            if next_idx == n - 1: return dist + 1
                            visited_indices.add(next_idx)
                            queue.append((next_idx, dist + 1))
                    # Efficiency: Clear the bucket once used
                    del prime_to_indices[p]
                used_prime_portals.add(p)
                    
        return -1
