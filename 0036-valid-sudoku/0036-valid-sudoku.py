class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Use dictionaries of sets for rows, columns, and boxes
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        boxes = {(i, j): set() for i in range(3) for j in range(3)}

        # Traverse the board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":  # Skip empty cells
                    continue

                # 1. Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # 2. Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # 3. Check the box
                box_key = (r // 3, c // 3)
                if val in boxes[box_key]:
                    return False
                boxes[box_key].add(val)

        # If no conflicts found, board is valid
        return True
