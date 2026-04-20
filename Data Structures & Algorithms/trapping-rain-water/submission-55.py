class Solution:
    def trap(self, height: List[int]) -> int:
        k = 0 
        binaries = [[] for _ in range(len(height))]
        for h in height:
            for _ in range(h):
                binaries[k].append(1)
            fill = max(height) - len(binaries[k])
            for _ in range(fill):
                binaries[k].append(0)
            k += 1

        trans = [list(row) for row in zip(*binaries)]
        count = [[] for _ in range(len(trans))]
        l = 0
        for group in trans:
            if l < len(count):
                for i, b in enumerate(group):
                    if b == 1:
                        count[l].append(i)
                l += 1
        
        sums = []
        for i, group in enumerate(count):
            group.sort(reverse=True)
            for i, x in enumerate(group):
                if i < (len(group)-1):
                    dif = x - group[i+1] - 1
                    sums.append(dif)

        return (sum(sums))

        

















