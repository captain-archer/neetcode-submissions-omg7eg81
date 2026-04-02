class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums[i] + nums[j] == target
        # i != j
        s = []
        v = []

        n = len(nums)
        # print(n)

        for x in range(n):
            s.append(x)

        #print(s)
        
        for x in range(n):
            temp = s.copy()
            temp.pop(x)
            v.append(temp)

        i = 0
        result = []
        # print(v)

        for x in range(n):
            case = v[i]
            for y in range(n-1):
                a = nums[i]
                b = nums[case[y]]
                if a + b == target:
                    result.append(i)
                    result.append(case[y])
                    result.sort()
                    return result
            i += 1




