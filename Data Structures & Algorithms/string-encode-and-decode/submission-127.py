class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []
        for x in strs:
            l = len(x)
            enc.append(f'{l}#')
            enc.append(x)

        s = ''.join(enc)
        return s

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            # Find the delimiter '#' starting from the current index
            j = s.find('#', i)
            # Extract the length of the string
            length = int(s[i:j])
            # Move pointer to the start of the actual string
            start = j + 1
            end = start + length
            # Extract the string and add to result
            dec.append(s[start:end])
            # Move pointer to the next length-prefix
            i = end
        
        return dec