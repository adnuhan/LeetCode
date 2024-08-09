class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        min_row = []
        max_column = []

        for i in matrix:
            min_row.append(min(i))

        for j in range(len(matrix[0])):
            mx = matrix[0][j]
            for k in range(1, len(matrix)):
                if matrix[k][j] > mx :
                    mx = matrix[k][j]
            max_column.append(mx)

        return list(set(min_row) & set(max_column))
        