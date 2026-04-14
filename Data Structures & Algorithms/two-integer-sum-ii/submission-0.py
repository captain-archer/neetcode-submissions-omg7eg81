class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 1 
        j = len(numbers)
        while numbers[i-1] + numbers[j-1] != target:
            if numbers[i-1] + numbers[j-1] > target:
                j -= 1
            else:
                i += 1
        
        return [i, j]
        