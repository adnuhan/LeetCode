class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        x = 0

        while x < len(arr):
            if arr[x] == 0:
                arr.insert(x + 1, 0)
                x += 1
                arr.pop()
            x += 1
