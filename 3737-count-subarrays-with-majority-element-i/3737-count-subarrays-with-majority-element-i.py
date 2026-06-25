
            target_count = 0
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                
                length = j - i + 1
                if 2 * target_count > length:
                    total_subarrays += 1
                    
        return total_subarrays