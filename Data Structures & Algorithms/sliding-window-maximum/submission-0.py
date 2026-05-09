class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        stack = []
        dif = len(nums) - k

        for i, num in enumerate(nums):
            if i <= dif:
                stack.append(max(nums[i:k]))
                k += 1

        return stack

        