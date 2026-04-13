class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Each row must contain the digits 1-9 without duplicates.
        count = 0
        for x in board:
            for y in x:
                if y.isdigit():
                    count += 1
        
        print(count)

        rowdup = 0
        row1_9 = 0
        for x in board:
            xfilter = [z for z in x if z != '.']
            if len(xfilter) == len(set(xfilter)):
                rowdup += 1
            for y in x:
                if y != '.':
                    if int(y) >= 1 and int(y) <= 9:
                        row1_9 += 1

        print(rowdup) # = 9, no duplicates
        print(row1_9) # = 25, numbers between 1-9

        #Each column must contain the digits 1-9 without duplicates.

        columns = [['.'] for _ in range(9)]

        n = 0
        n1 = 0
        for x in range(9):
            for y in range(9):
                b = board[n]
                #columntorow.append(b[n1])
                columns[n1].append(b[n1])
                n += 1
            n1 += 1
            n = 0
        
        print()

        columndup = 0
        column1_9 = 0
        for x in columns:
            xfilter = [z for z in x if z != '.']
            if len(xfilter) == len(set(xfilter)):
                columndup += 1
            for y in x:
                if y != '.':
                    if int(y) >= 1 and int(y) <= 9:
                        column1_9 += 1

        print(columndup)
        print(column1_9)

        boxes = [[] for _ in range(9)]

        for box_row in range(3):
            for box_col in range(3):
                box_index = box_row * 3 + box_col

                for i in range(3):
                    for j in range(3):
                        row = box_row * 3 + i
                        col = box_col * 3 + j
                        boxes[box_index].append(board[row][col])
                
        boxdup = 0
        box1_9 = 0

        for x in boxes:
            xfilter = [z for z in x if z != '.']
            if len(xfilter) == len(set(xfilter)):
                boxdup += 1
            for y in x:
                if y != '.':
                    if int(y) >= 1 and int(y) <= 9:
                        box1_9 += 1

        print(boxdup)
        print(box1_9)

        if (rowdup == 9 and
            row1_9 == count and
            columndup == 9 and
            column1_9 == count and
            boxdup == 9 and
            box1_9 == count):
            return True
        else:
            return False

        #Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.


        