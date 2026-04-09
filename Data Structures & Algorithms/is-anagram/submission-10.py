class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s1 = [0] * 26
        t1 = [0] * 26

        for x in s:
            pos = ord(x) - ord('a')
            s1[pos] += 1

        for x in t:
            pos = ord(x) - ord('a')
            t1[pos] += 1

        if t1 == s1:
            return True
        else:
            return False

