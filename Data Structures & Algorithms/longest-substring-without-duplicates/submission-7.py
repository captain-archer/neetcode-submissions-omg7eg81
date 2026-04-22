class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        print(len(s))
        if len(s) == 0:
            return 0
        sets = []
        sizes = []

        for char in s:
            sets.append(char)
            temp = set(sets)
            if len(temp) == len(sets):
                sizes.append(len(temp))
            else:
                sets.pop(0)
                sizes.append(len(temp))

        print(sets)
        print(sizes)
        return max(sizes)
            


        