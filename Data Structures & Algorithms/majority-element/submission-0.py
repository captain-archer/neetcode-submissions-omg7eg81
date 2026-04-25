class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums) / 2
        uniq = set(nums)

        data = {}

        for x in uniq:
            data[x] = 0

        for x in nums:
            data[x] += 1

        for key, value in data.items():
            if value > n:
                return key


        