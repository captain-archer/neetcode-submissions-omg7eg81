# bucket solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i, word in enumerate(strs):
            sort = ''.join(sorted(word))
            #if sort in  
            d.setdefault(sort, []).append(word)
            #d[sort] = word


        result = list(d.values())
        return result

        