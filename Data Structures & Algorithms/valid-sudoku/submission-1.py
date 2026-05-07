class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create list of rows
        rows = [[] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                # ignore '.' characters
                if board[r][c] != '.':
                    rows[r].append(board[r][c])
        # create list of cols
        cols = [[] for _ in range(9)]
        for c in range(9):
            for r in range(9):
                # ignore '.' characters
                if board[r][c] != '.':
                    cols[c].append(board[r][c])
        # do the same for boxes
        # (i // 3 == 0) row indices 0, 1, or 2 --> box indices 0, 1, or 2
        # (i // 3 == 1) row indices 3, 4, 5 --> box indices 3, 4, 5
        # (i // 3 == 2) row indices 6, 7, 8 --> box indices 6, 7, 8
        # (j // 3 == 0) col indices 0, 1, 2 --> box indices 0, 3, 6
        # (j // 3 == 1) col indices 3, 4, 5 --> box indices 1, 4, 7
        # (j // 3 == 2) col indices 6, 7, 8 --> box indices 2, 5, 8
        # box index = 3 * (i // 3) + (j // 3)
        boxes = [[] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                # ignore '.' characters
                if board[r][c] != '.':
                    i = (3 * (r // 3)) + c // 3
                    boxes[i].append(board[r][c])

        # check for duplicates using hash set
        for row in rows:
            if len(row) != len(set(row)):
                return False

        for col in cols:
            if len(col) != len(set(col)):
                return False

        for box in boxes:
            if len(box) != len(set(box)):
                return False

        return True
        