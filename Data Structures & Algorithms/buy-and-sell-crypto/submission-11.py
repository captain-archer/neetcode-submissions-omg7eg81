class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        inds = []

        for i in range(len(prices)-1):
            for j in range(i + 1, len(prices)):
                soma = (prices[i] - prices[j]) * (-1)
                print(soma)
                if soma >= 0:
                    res.append(soma)

        print(res)
        if res == []:
            return 0

        return max(res)

                
        