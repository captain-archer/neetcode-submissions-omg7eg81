class Solution:
    def maxDifference(self, s: str) -> int:

        data = {}

        for x in s:
            if x not in data:
                data[x] = 1
            else:
                data[x] += 1
        
        print(data)

        values = list(data.values())
        print(values)
        even = []
        odd = []

        for x in values:
            if x % 2 == 0:
                even.append(x)
                print('e',x)
            else:
                odd.append(x)
                print('o',x)

        print(odd)  #1
        print(even) #3
        res = []

        print(res)

        return max(odd) - min(even)
            
        