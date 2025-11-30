from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initial window sum: first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window from index k to end
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k
