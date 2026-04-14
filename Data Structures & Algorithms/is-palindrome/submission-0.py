class Solution:
    def isPalindrome(self, s: str) -> bool:

        self = s.replace(" ", "")
        self = "".join(c for c in s if c.isalnum())
        self = self.lower()
        rev = self[::-1]
        rev = rev.lower()
        #print(self)
        #print(rev)
        
        count = 0
        i = 0
        for _ in range(len(self)):
            if self[i] == rev[i]:
                count += 1
            else:
                return False
            i += 1

        #print(len(self))
        #print(count)

        if count == len(self):
            return True

