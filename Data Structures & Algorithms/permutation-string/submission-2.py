class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        sorted1 = sorted(s1)
        t = []
        c = 0
        for i, x in enumerate(s2):
            if i < (len(s2)-len(s1)+1):
                for k in range(len(sorted1)):
                    t.append(s2[i+k])
                sortedt = sorted(t) 
                if sortedt == sorted1:
                    return True
                c += 1
                t = []
        
        if c == (len(s2)-len(s1)+1):
            return False





        