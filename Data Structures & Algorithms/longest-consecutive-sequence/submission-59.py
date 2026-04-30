class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0 
        nums = set(nums)
        num = min(nums)
        max_ = max(nums)
        #print(nums)
        #print(num)
        #data = {}
        count = 0
        counts = []
        while num <= max_:
            if num in nums:
                num += 1
                count += 1
                nums.remove(num-1)
            else:
                counts.append(count)
                count = 0
                num += 1
        
        counts.append(count)
        #print(counts)
        return max(counts)

        