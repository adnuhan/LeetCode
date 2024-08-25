class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        return sum([abs(sorted(seats)[i] - sorted(students)[i]) for i in range(len(seats))])
