class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        integer = [num for num in range(left, right + 1)]

        for start, end in ranges:
            for n in range(start, end+1):
                if n in integer:
                    integer.remove(n)

        return len(integer) == 0
