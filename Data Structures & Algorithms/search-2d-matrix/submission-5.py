class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        aim = []
        for i, row in enumerate(matrix):
            if row[-1] < target:
                continue
            if row[-1] >= target:
                aim = matrix[i]
                break

        if len(matrix) == 1:
            for x in matrix[0]:
                if x == target:
                    return True
            return False
        
        if target in aim:
            return True
        else:
            return False
