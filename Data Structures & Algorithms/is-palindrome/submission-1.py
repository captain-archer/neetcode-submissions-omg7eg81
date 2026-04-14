class Solution:
    def isPalindrome(self, s: str) -> bool:
        self = s.replace(" ", "")
        self = "".join(c for c in s if c.isalnum())
        self = self.lower()   
        print(len(self))
        count = 0
        i = 0
        #for i in range(len(self)):
        for j in range(len(self)-1, -1, -1):
            if self[i] == self[j]:
                count += 1
            i += 1

        if count == len(self):
            return True
        else:
            return False
