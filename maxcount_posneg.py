import bisect
from typing import List


"""
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.
"""


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Number of negatives: index where 0 would be inserted, all before are < 0
        print(nums)
        neg = bisect.bisect_left(nums, 0)
        print(neg)
        # Number of positives: total length minus index where all after are > 0
        pos = len(nums) - bisect.bisect_right(nums, 0)
        print(pos)
        # Return the maximum of the two counts
        return max(neg, pos)


if __name__ == "__main__":
    nums = [-3, -2, -1, 0, 0, 1, 3]
    print(Solution().maximumCount(nums))
