from typing import List

"""
Given an array nums containing n distinct numbers taken from the range [0, n], return the one that is missing from the array.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == "__main__":
    nums = [1, 2]
    print(Solution().missingNumber(nums))
