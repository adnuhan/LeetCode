class Solution:
    def minimumSum(self, num: int) -> int:

        num_list = list(str(num))
        num_list.sort()

        return int(num_list[0] + num_list[3]) + int(num_list[1] + num_list[2])
