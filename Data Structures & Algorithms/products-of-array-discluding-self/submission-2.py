class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # without using the division operation?

        out = []
        for i, x in enumerate(nums):
            pop = nums[:i] + nums[i+1:]
            j = 0
            result = pop[j]
            while j < (len(pop) - 1):
                result *= pop[j+1]
                j += 1
            out.append(result)
    
        return out
        