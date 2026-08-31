class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for x in range(9)]

        #review
        boxes = {}
        for i, row in enumerate(board):
            seen = set()
            for j, col in enumerate(row):
                if col != ".":
                    #print(f'row: {row} | col: {col}')
                    # checking row
                    if col in seen:
                        return False
                    # checking col
                    if col in cols[j]:
                        return False

                    # 3x3 box check
                    box = (i // 3, j // 3)

                    if box not in boxes:
                        boxes[box] = set()

                    if col in boxes[box]:
                        return False
                    
                    seen.add(col)
                    cols[j].add(col)
                    boxes[box].add(col)

        return True
