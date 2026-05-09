class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        stack = []
        dif = len(nums) - k
        i = 0

        for _ in range(dif+1):
            stack.append(max(nums[i:k]))
            k += 1
            i += 1

        return stack

        