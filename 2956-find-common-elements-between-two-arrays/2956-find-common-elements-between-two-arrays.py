class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        output = [0, 0]

        for x in nums1:
            if x in nums2:
                output[0] += 1

        for y in nums2:
            if y in nums1:
                output[1] += 1

        return output
