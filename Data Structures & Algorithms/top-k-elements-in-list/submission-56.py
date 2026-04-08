class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        sets = list(set(nums))

        lst = list(sets)
        print(lst)

        # lst.sort(reverse=True)
        # print(lst)

        qtd = [0] * len(lst)
        for i, num in enumerate(lst):
            for x in nums:
                if num == x:
                    qtd[i] += 1
                    
        print()
        print(qtd)
        #last = qtd[-k:]
        #value = (len(qtd) - 1) - k

        #qtd.sort(reverse=False)
        #print('qtd ordem', qtd)

        # qtd1 = list(set(qtd))
        # qtd = list(qtd1)

        # result = []
        # for i, num in enumerate(qtd):
        #     if i > value:
        #         result.append(i)

        res = []
        print()

        #largest = sorted(qtd, reverse=True)[:k]

        topk = set(sorted(qtd, reverse=True)[:k])
        largneg = [x if x in topk else -1 for x in qtd]

        print(largneg)
        
        for i, x in enumerate(largneg):
            if x >= 0:
                res.append(lst[i])
        print(largneg)
        print(res)
        #for x in result:
        #    res.append(lst[x])


        #result.sort(reverse=True)
        return res

        #return (lst[-k:])