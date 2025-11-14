
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result

# Test cases to verify the solution
def test_shuffle():
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 5, 1, 3, 4, 7]
    n1 = 3
    result1 = solution.shuffle(nums1, n1)
    print(f"Input: nums = {nums1}, n = {n1}")
    print(f"Output: {result1}")
    print(f"Expected: [2, 3, 5, 4, 1, 7]")
    print(f"Pass: {result1 == [2, 3, 5, 4, 1, 7]}")
    print()
    
    # Test case 2
    nums2 = [1, 2, 3, 4, 4, 3, 2, 1]
    n2 = 4
    result2 = solution.shuffle(nums2, n2)
    print(f"Input: nums = {nums2}, n = {n2}")
    print(f"Output: {result2}")
    print(f"Expected: [1, 4, 2, 3, 3, 2, 4, 1]")
    print(f"Pass: {result2 == [1, 4, 2, 3, 3, 2, 4, 1]}")
    print()
    
    # Test case 3
    nums3 = [1, 1, 2, 2]
    n3 = 2
    result3 = solution.shuffle(nums3, n3)
    print(f"Input: nums = {nums3}, n = {n3}")
    print(f"Output: {result3}")
    print(f"Expected: [1, 2, 1, 2]")
    print(f"Pass: {result3 == [1, 2, 1, 2]}")
    print()

# Alternative implementations for comparison
class AlternativeSolutions:
    def shuffle_zip(self, nums: List[int], n: int) -> List[int]:
        result = []
        for x, y in zip(nums[:n], nums[n:]):
            result.extend([x, y])
        return result
    
    def shuffle_comprehension(self, nums: List[int], n: int) -> List[int]:
        return [nums[i // 2 + (i % 2) * n] for i in range(2 * n)]
    
    def shuffle_inplace(self, nums: List[int], n: int) -> List[int]:
        # This modifies the original array
        for i in range(n, 2 * n):
            nums.insert(2 * (i - n) + 1, nums[i])
            nums[i + 1] = 0  # Placeholder
        # Remove placeholders
        return [x for x in nums if x != 0]

# Compare all methods
def compare_methods():
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    
    sol = Solution()
    alt = AlternativeSolutions()
    
    print("Comparing different methods:")
    print(f"Original array: {nums}")
    print(f"Main method: {sol.shuffle(nums, n)}")
    print(f"Zip method: {alt.shuffle_zip(nums, n)}")
    print(f"Comprehension method: {alt.shuffle_comprehension(nums, n)}")
    print(f"In-place method: {alt.shuffle_inplace(nums.copy(), n)}")

# Run the tests
if __name__ == "__main__":
    print("Testing shuffle function:\n")
    test_shuffle()
    print("\n" + "="*50 + "\n")
    compare_methods()