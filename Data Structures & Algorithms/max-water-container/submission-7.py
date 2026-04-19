class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Find amount of pairs
        c = len(heights)-1
        pairs = 0
        for _ in range(len(heights)-1):
            pairs += c
            c -= 1

        i = 0
        j = 1
        k = len(heights)-1
        p = 0
        areas = []
        while p < pairs+1:
            for _ in range(k):
                d = len(heights[i:j])
                h = min(heights[i],heights[j])
                area = h * d
                areas.append(area)
                j += 1
            i += 1
            k -= 1
            j -= k
            p += 1
        
        return max(areas)
