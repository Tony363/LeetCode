class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i - 1 to prevent exceeding index limit 0
        i = m+n-1
        # iterate back wards
        while(n>=1 and m >=1):
            # if ith nums2 greater than ith nums1
            if nums2[n-1]>=nums1[m-1]:
                # assign it in reverse order
                nums1[i] = nums2[n-1]
                # decrement ith for nums2
                n-=1
            else :
                # assign it in reverse order
                nums1[i] = nums1[m-1]
                # decrement ith for nums1
                m-=1
            # decrement ith for output nums1
            i-=1
        if n>=1:
            nums1[i::-1] = nums2[n-1::-1]