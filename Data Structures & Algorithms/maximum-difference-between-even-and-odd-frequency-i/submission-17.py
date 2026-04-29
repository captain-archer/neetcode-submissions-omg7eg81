class Solution:
    def maxDifference(self, s: str) -> int:

        data = {}

        for x in s:
            if x not in data:
                data[x] = 1
            else:
                data[x] += 1

        values = list(data.values())
        even = []
        odd = []

        for x in values:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)

        return max(odd) - min(even)
            
        