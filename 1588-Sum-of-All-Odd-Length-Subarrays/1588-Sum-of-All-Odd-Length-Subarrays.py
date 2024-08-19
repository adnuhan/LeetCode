class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        output = sum(arr)
        odd = 3

        while odd <= len(arr):
            curr_sum = sum(arr[:odd]) 
            output += curr_sum
            for i in range(odd, len(arr)):
                curr_sum = curr_sum + arr[i] - arr[i - odd]
                output += curr_sum
            odd += 2

        return output
    
