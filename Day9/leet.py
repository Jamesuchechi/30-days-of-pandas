class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for n in nums:
            if n <= first:
                first = n           # new smallest number
            elif n <= second:
                second = n          # n is greater than first but smaller than second
            else:
                return True         # n > first and n > second -> triplet found

        return False
