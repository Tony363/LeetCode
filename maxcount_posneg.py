import bisect
from typing 


"""
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.
"""
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Number of negatives: index where 0 would be inserted, all before are < 0
        neg = bisect.bisect_left(nums, 0)
        # Number of positives: total length minus index where all after are > 0
        pos = len(nums) - bisect.bisect_right(nums, 0)
        # Return the maximum of the two counts
        return max(neg, pos)
