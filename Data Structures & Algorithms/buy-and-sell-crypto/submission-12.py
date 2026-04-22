class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []

        for i in range(len(prices)-1):
            for j in range(i + 1, len(prices)):
                soma = (prices[i] - prices[j]) * (-1)
                if soma >= 0:
                    res.append(soma)

        if res == []:
            return 0

        return max(res)

                
        