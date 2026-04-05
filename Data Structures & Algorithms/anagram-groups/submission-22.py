class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        #code here
        freq = {}
        
        for word in strs:
            count = [0] * 26
            
            for ch in word:
                count[ord(ch) - ord('a')] +=1
                
            key = tuple(count)
            
            if key not in freq:
                freq[key] = []
                
            freq[key].append(word)
            
        
        res = []
        for val in freq.values():
            res.append(val)
            
        return res